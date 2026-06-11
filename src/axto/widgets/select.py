from axto.widgets.base import Widget
from axto.keys import Key

class Select(Widget):
    def __init__(self, x, y, width, options: list, default_index=0, label=""):
        super().__init__(x, y, width=width, height=1, selectable=True)
        
        self.options = options
        self.selected_index = default_index
        self.label = label

    def on_key(self, key):
        if key == Key.LEFT:
            if self.selected_index > 0:
                self.selected_index -= 1
                self.trigger("change", self.options[self.selected_index], self.selected_index)
                
        elif key == Key.RIGHT:
            if self.selected_index < len(self.options) - 1:
                self.selected_index += 1
                self.trigger("change", self.options[self.selected_index], self.selected_index)

    def draw(self, term):
        color = self.theme.widget_selected if self.selected else self.theme.widget_deselected
        current_value = self.options[self.selected_index]
        display_label = f"{self.label}: " if self.label else ""
        
        main_text = f"{display_label}< {current_value} >"
        
        term.move_cursor(self.x, self.y)
        term.write(main_text[:self.width].ljust(self.width), color)
