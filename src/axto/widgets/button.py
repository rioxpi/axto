from axto.widgets.base import Widget
from axto.keys import Key

class Button(Widget):
    def __init__(self, x, y, text):
        super().__init__(x, y, len(text) + 4, 1)  # Width based on text length + padding
        self.text = text
    
    def on_key(self, key):
        """If is focused and Enter is pressed, trigger the button action."""
        if key == Key.ENTER:
            self.trigger("press")
    
    def draw(self, term):
        """Drawing the button depends on whether it's selected or not."""
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