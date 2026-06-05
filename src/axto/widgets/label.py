from axto.widgets.base import Widget
from axto.styles import Color

class Label(Widget):
    def __init__(self, x, y,text,height:int=None, color:str=Color.WHITE, align="left", width=None):
        self.initial_text = text

        lines = text.split("\n")
        max_line_length = max(len(line) for line in lines) if lines else 0

        chosen_width = width if width is not None else max_line_length
        chosen_height = height if height is not None else len(lines)

        super().__init__(x, y, width=chosen_width, height=chosen_height, selectable=False)

        self.text = text
        self.color = color
        self.align = align  # "left", "right", "center"

    def draw(self, term):
        """Render the label widget.

        Args:
            term (Terminal): Terminal instance used for rendering
        """
        lines = self.text.split("\n")

        for i in range(self.height):
            if i < len(lines):
                line = lines[i][:self.width]
            else:
                line = ""

            # Alignment
            if len(line) < self.width:
                if self.align == "right":
                    line = line.rjust(self.width)
                elif self.align == "center":
                    line = line.center(self.width)
                else:
                    line = line.ljust(self.width)

            term.move_cursor(self.x, self.y + i)
            term.write(line, self.color)

    def set_text(self, text, resize=True):
        """Update the label's text.
        
        Args:
            text (str): The new text to display.
            resize (bool): If True, width will adapt to the new text length.
                           If False, text will be clipped/padded to current width.
        """
        self.text = text

        if resize:
            lines = text.split("\n")
            self.width = max(len(line) for line in lines) if lines else 0
            self.height = len(lines)
