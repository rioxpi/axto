from axto.widgets.base import Widget

class Container(Widget):
    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float, has_border: bool=True, title:str = ""):
        super().__init__(x, y, width, height, False)
        self.children = []
        self.has_border = has_border
        self.title = title
    
    def add_child(self, widget: Widget):
        """_summary_

        Args:
            widget (Widget): _description_
        """
        if hasattr(self, "engine") and self.engine:
            widget.engine = self.engine
        self.children.append(widget)
        return widget

    def resolve_geometry(self, parent_w: int, parent_h: int) -> None:
        super().resolve_geometry(parent_w, parent_h)
        
        for child in self.children:
            child.resolve_geometry(self.width, self.height)
            
            border_offset = 1 if self.has_border else 0
            child.x = self.x + child.x + border_offset - 1
            child.y = self.y + child.y + border_offset - 1
    
    def draw(self, term):
        if self.has_border:
            color = self.theme.border_normal
            
            title_part = f"┤ {self.title} ├" if self.title else ""
            edge_len = (self.width - 2 - len(title_part)) // 2
            top_line = "┌" + "─" * edge_len + title_part + "─" * (self.width - 2 - edge_len - len(title_part)) + "┐"
            term.move_cursor(self.x, self.y)
            term.write(top_line[:self.width], color)

            for i in range(1, self.height - 1):
                term.move_cursor(self.x, self.y + i)
                term.write("│", color)
                term.move_cursor(self.x + self.width - 1, self.y + i)
                term.write("│", color)
            
            term.move_cursor(self.x, self.y + self.height - 1)
            term.write(("└" + "─" * (self.width - 2) + "┘")[:self.width], color)