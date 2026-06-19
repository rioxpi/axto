from axto.widgets.base import Widget
from axto.widgets import Label

class PopUp(Widget):
    def __init__(self, x: int | float, y: int | float, title : str, message: str):        
        super().__init__(x, y, width=1, height=1, selectable=False)
        self.message = message
        self.title = title
        self._raw_w = 0.4
                
    def resolve_geometry(self, parent_w: int, parent_h: int) -> None:
        lines = self.message.splitlines()
        
        max_line_len = max(len(l) for l in lines) if lines else 0
        
        calculated_w = max(max_line_len + 4, len(self.title) + 6, 30)
        calculated_h = len(lines) + 4
        
        self.width = calculated_w
        self.height = calculated_h
        
        super().resolve_geometry(parent_w, parent_h)
    
        self.width = calculated_w
        self.height = calculated_h
        
    def draw(self, term) -> None:
        color = self.theme.information_color
        lines = self.message.splitlines()
        
        term.move_cursor(self.x, self.y)
        title_part = f"┤ {self.title} ├"
        dash_count = self.width - 2 - len(title_part)
        left_dashes = dash_count // 2
        right_dashes = dash_count - left_dashes
        top_line = "┌" + "─" * left_dashes + title_part + "─" * right_dashes + "┐"
        term.write(top_line[:self.width],color)
        
        term.move_cursor(self.x, self.y + 1)
        term.write("│" + " " * (self.width - 2) + "│", color)
        
        for idx, l in enumerate(lines):
            term.move_cursor(self.x, self.y + 2 + idx)
            content = l.ljust(self.width - 4)[:self.width - 4]
            full_row = f"│ {content} │"
            term.write(full_row, color)
        
        term.move_cursor(self.x, self.y + self.height - 2)
        term.write("│" + " " * (self.width -2) + "│", color)
        
        term.move_cursor(self.x, self.y + self.height - 1)
        bottom_line = "└" + "─" * (self.width -  2) + "┘"
        term.write(bottom_line[:self.width], color)