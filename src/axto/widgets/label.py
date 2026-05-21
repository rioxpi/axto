from axto.widgets.base import Widget

class Label(Widget):
    def __init__(self, x, y, text, color="73"):
        super().__init__(x,y, width=len(text), height=1, selectable=False)
        self.text = text
        self.color = color
    
    def draw(self, term):
        """Render the label widget

        Args:
            term (Terminal): Terminal instance used for rendering
        """
        term.move_cursor(self.x, self.y)
        term.write(self.text, self.color)
    
    def set_text(self, text):
        """Update the label's text and adjust width accordingly

        Args:
            text (str): The new text to display in the label
        """
        self.text = text
        self.width = len(text)