import sys
import tty
import termios
import signal
import time
from .terminal import Terminal
from .parser import read_key
from .keys import Key
from .styles import Theme
from .default_scenes import DefaultScenes
from .widgets.pop_up import PopUp
import queue

class Engine:
    """
    Core engine that runs the application, manages the main loop, and handles input and rendering
    """
    def __init__(self):
        self.running = False
        self.widgets = []
        self._old_settings = None
        self.focus_index = -1 # Index of the currently focused widget
        self.theme = Theme()
        
        self.min_size = (0,0)
        
        self.default_scenes = DefaultScenes(self)
        
        self.main_thread_queue = queue.Queue()
        
        self._widget_data = []
        self._is_terminal_too_small = False 
        
        self._active_popup = ()
        
        if hasattr(signal, 'SIGWINCH'):
            signal.signal(signal.SIGWINCH, self._handle_sigwinch)
        
        
    def add_widget(self, widget):
        """Add a widget to the engine's list of widgets

        Args:
            widget (Widget): The widget to add
        """
        widget.engine = self
        self.widgets.append(widget)
        self._widget_data.append(widget)
        data = Terminal.get_size()
        widget.resolve_geometry(data[0], data[1])

    def _enable_raw_mode(self):
        """
        Change terminal to raw mode to read input byte by byte
        """
        fd = sys.stdin.fileno()
        self._old_settings = termios.tcgetattr(fd)
        tty.setraw(fd)
        Terminal.hide_cursor()

    def _disable_raw_mode(self):
        """
        Restore standard terminal settings
        """
        if self._old_settings:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self._old_settings)
        
        Terminal.show_cursor()

    def run(self):
        """
        Run the application
        """
        self.running = True
        self._enable_raw_mode()
        
        try:
            Terminal.clear_screen()
            
            # Focus the first widget if it exists
            self._next_widget() 
            
            self._handle_resize()  # Initial render based on current terminal size
            
            while self.running:    
                                
                self._process_main_thread_queue()
                
                self._check_popup_timeout()
                
                # Draw all widgets 
                self._render_all_widgets()
                
                # Handle input
                key = read_key()
                self._handle_input(key)
                
                if self.widgets and key:
                    active_widget = self.all_active_widgets[self.focus_index]
                    active_widget.on_key(key)
        finally:
            # Restore terminal settings and clear screen on exit
            self._disable_raw_mode()
            Terminal.clear_screen()
    
    def _render_all_widgets(self):
        """
        Helper method to render all widgets
        """
        Terminal.clear_screen()
        for widget in self.all_active_widgets:
            widget.draw(Terminal)
            
        if self._active_popup:
            self._active_popup[0].draw(Terminal)
    
    def _next_widget(self):
        """
        Move focus to the next widget
        """
        
        widgets = self.all_active_widgets
        
        if not widgets: 
            return
        
        # Checking for selectable widget
        if not any(w.is_selectable for w in widgets):
            if self.focus_index != -1:
                widgets[self.focus_index].deselect()
            self.focus_index = -1
            return
        
        if self.focus_index != -1: 
            widgets[self.focus_index].deselect()  # Deselect current widget
        
        old_index = self.focus_index
        while True:
            self.focus_index = (self.focus_index + 1) % len(widgets)
            if widgets[self.focus_index].is_selectable:
                break
            if self.focus_index == old_index:  
                return
        
        widgets[self.focus_index].select()  # Select new widget

    def _handle_input(self, key):
        """
        Handle user input
        """
        if key == '\x03' or key == Key.ESC or key == "\x11":  # Quit on Ctrl+C, Escape key or Ctrl+Q
            self.running = False
        elif key == Key.TAB:  # Tab key to switch focus
            self._next_widget()
    
    def _handle_sigwinch(self, signum, frame):
        """
        Handle terminal resize signal (SIGWINCH)
        """
        self._handle_resize()
    
    def _handle_resize(self):
        """
        Handle terminal resize events
        """
        if not self._is_terminal_too_small:
            self._widget_data = self.widgets
        
        width, height = Terminal.get_size()
        Terminal.clear_screen()
        
        if self.min_size != (0,0) and (width < self.min_size[0] or height < self.min_size[1]):
            self.default_scenes.construct_terminal_too_small(self.min_size)
            self.default_scenes.change_scene("terminal_too_small")
            self._is_terminal_too_small = True
        else:
            self.widgets = self._widget_data
            self._is_terminal_too_small = False
            
        time.sleep(0.01)
        
        for widget in self.widgets:
            widget.resolve_geometry(width, height)
        
        if self._active_popup:
            self._active_popup[0].resolve_geometry(width, height)
            
        
        self._render_all_widgets()
    
    def dispatch_to_main_thread(self, func, *args, **kwargs):
        """
        Safe execute function from thread
        
        Args:
            func (function): Function to execute
        """
        self.main_thread_queue.put((func, args, kwargs))
    
    def _process_main_thread_queue(self):
        """
        Processing functions from main_thread_queue
        """ 
        
        while not self.main_thread_queue.empty():
            try:
                func, args, kwargs = self.main_thread_queue.get_nowait()
                func(*args, **kwargs)
                self.main_thread_queue.task_done()
            except queue.Empty:
                break

    def add_popup(self, title: str, message: str, duration : float = 3.0) -> None:
        """ Create a popup widget and add it to the engine for a specified duration

        Args:
            title (str): Title of the popup
            message (str): Message content of the popup
            duration (float, optional): Duration for which the popup should be displayed. Defaults to 3.0.
        """
        
        expire_time = time.time() + duration
        
        widget = PopUp(0.4, 0.4, title, message)
        
        widget.engine = self
        
        w,h = Terminal.get_size()
        widget.resolve_geometry(w,h)
        
        self._active_popup = (widget, expire_time)
        
        self._render_all_widgets()
    
    def _check_popup_timeout(self) -> None:
        """ 
        Check if the active popup has expired and remove it if necessary 
        """
        
        if not self._active_popup: return
        
        expire_time = self._active_popup[1]
        
        now = time.time()
        
        if now >= expire_time:
            self._active_popup = ()
            self._render_all_widgets()
            
        
    
    @property
    def all_active_widgets(self) -> list:
        """Get all active widgets

        Returns:
            list: List of all active widgets
        """
        flat_list = []
        for w in self.widgets:
            flat_list.append(w)
            if hasattr(w, 'children'):
                flat_list.extend(w.children)
        return flat_list
