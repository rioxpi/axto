from axto.widgets.base import Widget
from axto.keys import Key
import time

class Input(Widget):
    def __init__(self, x, y, width, placeholder='', selectable=True):
        super().__init__(x, y, width, height=1, selectable=selectable)
        self.placeholder = placeholder
        self.text = ''
        self.error_until = 0  
    
    def on_key(self, key):
        """Handle key press events for the input widget.

        Args:
            key (Key): The key that was pressed. Can be a string or a Key enum.
        """
        if key == Key.ENTER:
            if not self.text: # Submit is not allowed if text is empty
                self.trigger_error_flash()
            else:
                self.trigger('submit', self.text)
        elif key == Key.BACKSPACE:
            self.text = self.text[:-1]
        elif len(key) == 1 and key.isprintable():
            self.text += key

    def trigger_error_flash(self):
        """
        Triggers a visual error flash effect.
        """
        self.error_until = time.time() + 0.3
    
    def draw(self, term):
        """Render the input widget.

        Args:
            term (Terminal): Terminal instance used for rendering
        """
        content_width = self.width - 2
        
        # Error efffect
        if time.time() < self.error_until:
            term.move_cursor(self.x, self.y)
            error_box = f"[{self.placeholder if not self.text else self.text}]".ljust(self.width)[:self.width]
            term.write(error_box, "1;37;41")
            return

        # Dynamic content and styling based on selection state
        if self.selected:
            bracket_color = "1;92"
            text_color = "0;37"
            
            # Calculate viewport for text based on cursor position
            cursor_pos = len(self.text)
            start_idx = max(0, cursor_pos - content_width)
            visible_text = self.text[start_idx:start_idx + content_width]
        
            left_bracket = "«" if start_idx > 0 else "<"
            right_bracket = "»" if len(self.text) > start_idx + content_width else ">"
        else:
            bracket_color = "2;37" 
            text_color = "2;37"
            
            visible_text = self.text[:content_width] if self.text else self.placeholder
            left_bracket = "["
            right_bracket = "]"

        padded_text = visible_text.ljust(content_width)[:content_width]

        # Rendering
        term.move_cursor(self.x, self.y)
        term.write(left_bracket, bracket_color)
        
        term.write(padded_text, text_color)
        
        term.write(right_bracket, bracket_color)

        if self.selected:
            actual_cursor_x = self.x + 1 + len(visible_text)
            
            term.move_cursor(actual_cursor_x, self.y)
            if hasattr(term, 'show_cursor'):
                term.show_cursor()
