from axto.widgets.base import Widget

class Box(Widget):
    """A box widget with rich visual styles and shadows."""
    
    # (TL, TR, BL, BR, HORIZ, VERT)
    BORDER_DESIGNS = {
        "single":    ("┌", "┐", "└", "┘", "─", "│"),
        "double":    ("╔", "╗", "╚", "╝", "═", "║"),
        "rounded":   ("╭", "╮", "╰", "╯", "─", "│"),
        "bold":      ("┏", "┓", "┗", "┛", "━", "┃"),
        "none":      (" ", " ", " ", " ", " ", " ")
    }

    def __init__(self, x, y, width, height,
                 border_style="single", selectable=True):
        super().__init__(x, y, width, height, selectable=selectable)
        
        if border_style not in self.BORDER_DESIGNS:
            raise ValueError(f"Unsupported border style. Use {list(self.BORDER_DESIGNS.keys())}")
        self.border_style = border_style
        
    def draw(self, term):
        color = self.theme.border_focus if self.selected else self.theme.border_normal
        tl, tr, bl, br, h, v = self.BORDER_DESIGNS[self.border_style]
        
        #draw_color = f"{color};{self.bg_color}" if self.bg_color else color
        inner_space = " " * (self.width - 2)

        term.move_cursor(self.x, self.y)
        term.write(f"{tl}{h * (self.width - 2)}{tr}", color)
        
        for i in range(1, self.height - 1):
            term.move_cursor(self.x, self.y + i)
            term.write(f"{v}{inner_space}{v}", color)
            
        
        term.move_cursor(self.x, self.y + self.height - 1)
        term.write(f"{bl}{h * (self.width - 2)}{br}", color)