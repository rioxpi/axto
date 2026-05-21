from axto.widgets.base import Widget
from axto.keys import Key

class Button(Widget):
    """A button widget.

    Args:
        Widget (Widget): The base widget class
    """
    def __init__(self, x, y, text, selectable=True):
        super().__init__(x, y, len(text) + 4, 1, selectable=selectable)
        self.text = text
    
    def on_key(self, key):
        """Handle key press events.

        Args:
            key (str, Key): The key that was pressed
        """
        if key == Key.ENTER:
            self.trigger("press")
    
    def draw(self, term):
        """Render the button widget.

        Args:
            term (Terminal): The terminal instance used for rendering
        """
        if self.selected:
            bracket_left = "<"
            bracket_right = ">"
            color = "1;32"  # Green for selected
        else:
            bracket_left = "["
            bracket_right = "]"
            color = "2;37"  # Dim white for unselected
        
        term.move_cursor(self.x, self.y)
        term.write(f"{bracket_left}{self.text}{bracket_right}", color)