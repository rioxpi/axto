from axto.widgets.base import Widget

class ProgressBar(Widget):
    def __init__(self, x:int|float, y:int|float, width:int|float, placeholder:str=""):
        super().__init__(x, y, width, 1, selectable=False)
        
        self.progress = 0.0
        self.placeholder = placeholder
    
    def set_progress(self, value: float) -> None:
        self.progress = max(0.0, min(value, 1.0))
    
    def draw(self, term) -> None:
        precent_string = f" {int(self.progress * 100)}%"
        
        bar_width = self.width - 2 - len(precent_string)
        
        if bar_width < 5:
            return

        filled_chars = int(self.progress * bar_width)
        remaining_chars = bar_width - filled_chars
        
        fill_char = "#"
        empty_char = "-"
        
        bar = (fill_char * filled_chars) + (empty_char * remaining_chars)
        
        display_text = f"[{bar}]{precent_string}"
        
        color = self.theme.progress_fill if self.progress >= 1.0 else self.theme.progress_complete
        
        term.move_cursor(self.x, self.y)
        term.write(display_text, color)