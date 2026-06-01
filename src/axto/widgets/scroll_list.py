from axto.widgets.base import Widget
from axto.keys import Key

class ScrollList(Widget):
    def __init__(self, x, y, width, height, items=None):
        super().__init__(x, y, width, height)
        self.items = items or []
        self.selected_index = 0
        self.scroll_offset = 0
    
    def on_key(self, key: Key):
        if not self.items: return
        
        if key == Key.UP:
            if self.selected_index > 0:
                self.selected_index -= 1
                if self.selected_index < self.scroll_offset:
                    self.scroll_offset -= 1
        elif key == Key.DOWN:
            if self.selected_index < len(self.items) - 1:
                self.selected_index += 1
                if self.selected_index >= self.scroll_offset + self.height:
                    self.scroll_offset += 1
    
    def draw(self, term):
        visible_items = self.items[self.scroll_offset : self.scroll_offset + self.height]
        
        for i, item in enumerate(visible_items):
            actual_index = self.scroll_offset + i 
            current_y = self.y + i
            
            if actual_index == self.scroll_offset + i and self.selected_index == actual_index:
                color = self.theme.list_item_selected
                prefix = '> '
            else:
                color = self.theme.list_item_normal
                prefix = ' '
            
            term.move_cursor(self.x, current_y)
            line_text = f"{prefix}{item}"[:self.width]
            term.write(line_text.ljust(self.width), color)