from axto.widgets.base import Widget

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
        return widget

    