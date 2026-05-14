from axto.widgets.base import Widget

class Box(Widget):
    def draw(self, term):
        color = "32" if self.selected else "37"
        
        # Draw top border
        term.move_cursor(self.x, self.y)
        term.write("┌" + "─" * (self.width - 2) + "┐", color)        
        
        # Draw sides
        for i in range(1, self.height - 1):
            term.move_cursor(self.x, self.y + i)
            term.write("|" + " " * (self.width - 2) + "|", color)
        
        # Draw bottom border
        term.move_cursor(self.x, self.y + self.height - 1)
        term.write("└" + "─" * (self.width - 2) + "┘    ", color)