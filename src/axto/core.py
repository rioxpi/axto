import sys
import tty
import termios
from .terminal import Terminal

class Engine:
    def __init__(self):
        self.running = False
        self.widgets = []
        self._old_settings = None
        self.focus_index = 0  # Index of the currently focused widget
        
    def add_widget(self, widget):
        self.widgets.append(widget)

    def _enable_raw_mode(self):
        """Change terminal to raw mode to read input byte by byte."""
        fd = sys.stdin.fileno()
        self._old_settings = termios.tcgetattr(fd)
        tty.setraw(fd)

    def _disable_raw_mode(self):
        """Restore standard terminal settings."""
        if self._old_settings:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self._old_settings)

    def run(self):
        self.running = True
        self._enable_raw_mode()
        
        try:
            Terminal.clear_screen()
            
            # Focus the first widget if it exists
            if self.widgets:
                self.widgets[self.focus_index].select() 
            
            while self.running:    
                # Draw all widgets 
                self._render_all_widgets()
                
                # 2. Handle input (reading 1 byte)
                # This blocks the loop until a key is pressed
                key = sys.stdin.read(1)
                self._handle_input(key)
                
                if self.widgets:
                    active_widget = self.widgets[self.focus_index]
                    active_widget.on_key(key)
        finally:
            # Restore terminal settings and clear screen on exit
            self._disable_raw_mode()
            Terminal.clear_screen()
    
    def _render_all_widgets(self):
        """Helper method to render all widgets."""
        for widget in self.widgets:
            widget.draw(Terminal)
    
    def _handle_input(self, key):
        """Handle user input"""
        if key == 'q':
            self.running = False
        elif key == '\t':  # Tab key to switch focus
            self.focus_index = (self.focus_index + 1) % len(self.widgets)
            index_before = (self.focus_index - 1) % len(self.widgets)
            self.widgets[index_before].deselect()  # Deselect previous widget
            self.widgets[self.focus_index].select()  # Select new widget