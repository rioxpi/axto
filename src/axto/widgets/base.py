class Widget:
    """
    Base class for all widgets
    """
    def __init__(self, x, y, width, height, selectable=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.handlers = {} 
        self.selected = False
        self.is_selectable = selectable

    def draw(self, term):
        """Render the widget

        Args:
            term (Terminal): The terminal instance used for rendering

        Raises:
            NotImplementedError: This method should be implemented by subclasses
        """
        raise NotImplementedError("Base Widget does not implement draw method")

    def on_key(self, key):
        """Handle key press events

        Args:
            key (str, Key): The key that was pressed
        """
        if "key" in self.handlers:
            self.handlers["key"](key)
    
    def trigger(self, event_name, *args, **kwargs):
        """Trigger an event handler if it exists

        Args:
            event_name (str): The name of the event to trigger
        """
        if event_name in self.handlers:
            self.handlers[event_name](*args, **kwargs)
    
    def bind(self, event_type, callback):
        """Bind an event handler to a specific event type

        Args:
            event_type (str): The type of event to bind
            callback (function): The function to call when the event occurs
        """
        self.handlers[event_type] = callback
    
    def select(self):
        """
        Called when the widget is selected/focused
        """
        self.selected = True
        self.trigger("select")

    def deselect(self):
        """
        Called when the widget is deselected/unfocused
        """
        self.selected = False
        self.trigger("deselect")