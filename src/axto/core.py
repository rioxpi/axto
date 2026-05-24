import sys
import tty
import termios
import signal
import time
from .terminal import Terminal
from .parser import read_key
from .keys import Key

class Engine:
    """
    Core engine that runs the application, manages the main loop, and handles input and rendering
    """
    def __init__(self):
        self.running = False
        self.widgets = []
        self._old_settings = None
        self.focus_index = 0  # Index of the currently focused widget
        if hasattr(signal, 'SIGWINCH'):
            signal.signal(signal.SIGWINCH, self._handle_sigwinch)
        
    def add_widget(self, widget):
        """Add a widget to the engine's list of widgets

        Args:
            widget (Widget): The widget to add
        """
        self.widgets.append(widget)

    def _enable_raw_mode(self):
        """
        Change terminal to raw mode to read input byte by byte
        """
        fd = sys.stdin.fileno()
        self._old_settings = termios.tcgetattr(fd)
        tty.setraw(fd)

    def _disable_raw_mode(self):
        """
        Restore standard terminal settings
        """
        if self._old_settings:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self._old_settings)

    def run(self): # TODO: Hide cursor
        """
        Run the application
        """
        self.running = True
        self._enable_raw_mode()
        
        try:
            Terminal.clear_screen()
            
            # Focus the first widget if it exists
            if self.widgets:
                self.widgets[self.focus_index].select() 
            
            self._handle_resize()  # Initial render based on current terminal size
            
            while self.running:    
                # Draw all widgets 
                self._render_all_widgets()
                #self._handle_resize()
                
                # 2. Handle input (reading 1 byte)
                # This blocks the loop until a key is pressed
                key = read_key()
                self._handle_input(key)
                
                if self.widgets:
                    active_widget = self.widgets[self.focus_index]
                    active_widget.on_key(key)
        finally:
            # Restore terminal settings and clear screen on exit
            self._disable_raw_mode()
            Terminal.clear_screen()
    
    def _render_all_widgets(self):
        """
        Helper method to render all widgets
        """
        for widget in self.widgets:
            widget.draw(Terminal)
    
    def _next_widget(self):
        """
        Move focus to the next widget
        """
        if not self.widgets: return
        
        self.widgets[self.focus_index].deselect()  # Deselect current widget
        
        old_index = self.focus_index
        while True:
            self.focus_index = (self.focus_index + 1) % len(self.widgets)
            if self.widgets[self.focus_index].is_selectable:
                break
            if self.focus_index == old_index:  # All widgets are non-selectable
                return
        
        self.widgets[self.focus_index].select()  # Select new widget

    def _handle_input(self, key):
        """
        Handle user input
        """
        if key == '\x03' or key == Key.ESC or key == "\x11":  # Quit on Ctrl+C, Escape key or Ctrl+Q
            self.running = False
        elif key == Key.TAB:  # Tab key to switch focus
            self._next_widget()
    
    def _handle_sigwinch(self, signum, frame):
        self._handle_resize()
    
    def _handle_resize(self):
        """
        Handle terminal resize events
        """
        width, height = Terminal.get_size()
        Terminal.clear_screen()
        
        time.sleep(0.01)
        
        for widget in self.widgets:
            widget.resolve_geometry(width, height)
        self._render_all_widgets()