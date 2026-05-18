from axto.widgets.base import Widget
from axto.keys import Key

class Input(Widget):
    def __init__(self, x, y, width, placeholder=''):
        super().__init__(x, y, width, height=1)
        self.placeholder = placeholder
        self.text = ''
    
    def on_key(self, key):
        """Handle key input for the input widget

        Args:
            key (str|Key): The key that was pressed. This can be a regular character or a special key from the Key enum.
        """
        if key == Key.ENTER:
            self.trigger('submit', self.text)
        elif key == Key.BACKSPACE:
            self.text = self.text[:-1]
        elif len(key) == 1 and key.isprintable():
            self.text += key
    
    def draw(self, term):
        """Render the input widget

        Args:
            term (Terminal): Terminal instance used for rendering
        """
        content_width = self.width - 2  # Account for borders
        if self.selected:
            color = "2;32"
            brackets = ("<", ">")
            display_text = self.text + "_" if len(self.text) < content_width else self.text
        else:
            color = "37"
            brackets = ("[", "]")
            display_text = self.text if self.text else self.placeholder
        
        formatted_text = display_text[:content_width].ljust(content_width)
        term.move_cursor(self.x, self.y)
        term.write(f"{brackets[0]}{formatted_text}{brackets[1]}", color)