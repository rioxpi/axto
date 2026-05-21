from axto.widgets.base import Widget

class Label(Widget):
    def __init__(self, x, y, text, color="73", align="left", width=None):
        self.initial_text = text
        chosen_width = width if width is not None else len(text)
        
        super().__init__(x, y, width=chosen_width, height=1, selectable=False)
        self.text = text
        self.color = color
        self.align = align  # Options: "left", "right", "center"

    def draw(self, term):
        """Render the label widget.

        Args:
            term (Terminal): Terminal instance used for rendering
        """
        display_text = self.text[:self.width]
        
        # Formatting text based on alignment
        if len(display_text) < self.width:
            if self.align == "right":
                display_text = display_text.rjust(self.width)
            elif self.align == "center":
                display_text = display_text.center(self.width)
            else:
                display_text = display_text.ljust(self.width)

        # Drawing the text
        term.move_cursor(self.x, self.y)
        term.write(display_text, self.color)

    def set_text(self, text, resize=False):
        """Update the label's text.
        
        Args:
            text (str): The new text to display.
            resize (bool): If True, width will adapt to the new text length.
                           If False, text will be clipped/padded to current width.
        """
        self.text = text
        if resize:
            self.width = len(text)
