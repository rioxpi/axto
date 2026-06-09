from axto.widgets.base import Widget
from axto.keys import Key

class CheckBox(Widget):
    """A checkbox widget.
    """
    def __init__(self, x, y, label="", checked=False):
        width = len(label) + 4 
        super().__init__(x, y, height=1, width=width)
        self.label = label
        self.checked = checked

    def toggle(self):
        """T
        oggles the checked state of the checkbox.
        """
        self.checked = not self.checked
        self.trigger("change", self.checked)
    
    def on_key(self, key):
        if key == Key.ENTER:
            self.toggle()
    
    def draw(self, term):
        check_symbol = "X" if self.checked else " "
        bracket_str = f"[{check_symbol}] "

        if self.selected:
            color = self.theme.widget_selected
        else:
            color = self.theme.widget_deselected

        term.move_cursor(self.x, self.y)
        full_text = f"{bracket_str}{self.label}"
        term.write(full_text[:self.width], color)