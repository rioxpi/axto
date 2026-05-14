from axto.widgets.base import Widget

class Box(Widget):
    def draw(self, term):
        # Draw top border
        term.move_cursor(self.x, self.y)
        term.write("┌" + "─" * (self.width - 2) + "┐")        
        
        # Draw sides
        for i in range(1, self.height - 1):
            term.move_cursor(self.x, self.y + i)
            term.write("|" + " " * (self.width - 2) + "|")
        
        # Draw bottom border
        term.move_cursor(self.x, self.y + self.height - 1)
        term.write("└" + "─" * (self.width - 2) + "┘    ")