from axto.widgets.base import Widget

class Box(Widget):
    def __init__(self, x, y, width, height, default_color="37", selected_color="32", border_style="single"):
        super().__init__(x, y, width, height)
        self.default_color = default_color
        self.selected_color = selected_color
        self.border_style = border_style
        if border_style not in ("single", "double", "none"):
            raise ValueError("Unsupported border style. Use 'single', 'double' or 'none'.")
        
    def draw(self, term):
        color = self.selected_color if self.selected else self.default_color
        
        # Draw top border
        term.move_cursor(self.x, self.y)
        if self.border_style == "single":
            term.write("┌" + "─" * (self.width - 2) + "┐", color)
        elif self.border_style == "double":
            term.write("╔" + "═" * (self.width - 2) + "╗", color)
        
        # Draw sides
        for i in range(1, self.height - 1):
            term.move_cursor(self.x, self.y + i)
            if self.border_style == "single":
                term.write("|" + " " * (self.width - 2) + "|", color)
            elif self.border_style == "double":
                term.write("║" + " " * (self.width - 2) + "║", color)
        
        # Draw bottom border
        term.move_cursor(self.x, self.y + self.height - 1)
        if self.border_style == "single":
            term.write("└" + "─" * (self.width - 2) + "┘    ", color)
        elif self.border_style == "double":
            term.write("╚" + "═" * (self.width - 2) + "╝    ", color)