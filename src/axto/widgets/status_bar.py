from .base import Widget

class StatusBar(Widget):
    def __init__(self, shortcuts : dict[str, str] = {}):
        super().__init__(0, 0, 1, 1, False)
        self.shortcuts = shortcuts
    
    def resolve_geometry(self, parent_w: int, parent_h: int) -> None:
        self.width = parent_w
        self.height = 1
        self.x = 0
        self.y = parent_h - 1
    
    def draw(self, term) -> None:
        parts = []
        for key, description in self.shortcuts.items():
            parts.append(f" [{key}] {description} ")
            
        status_text = "│".join(parts)
        
        full_line = " " + status_text
        if len(full_line) < self.width:
            full_line += " " * (self.width - len(full_line))
        else:
            full_line = full_line[:self.width]

        color = self.theme.widget_selected

        term.move_cursor(self.x, self.y)
        term.write(full_line, color)