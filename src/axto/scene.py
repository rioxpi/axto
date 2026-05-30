from axto.widgets.base import Widget
from axto.terminal import Terminal

class Scene:
    """
    It contains a list of widgets.
    """
    def __init__(self) -> None:
        self.widgets = []
    
    def add_widget(self, widget:Widget) -> Widget:
        """Add a widget to the scene

        Args:
            widget (Widget): The widget to add
        """
        self.widgets.append(widget)
        parent_w, parent_h = Terminal.get_size()
        widget.resolve_geometry(parent_w, parent_h)
        return widget

    
