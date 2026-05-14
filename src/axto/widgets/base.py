class Widget:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.handlers = {} 
        self.selected = False

    def draw(self, term):
        raise NotImplementedError("Base Widget does not implement draw method")

    def on_key(self, key):
        """Default key handler, can be overridden by subclasses"""
        if "key" in self.handlers:
            self.handlers["key"](key)
    
    def bind(self, event_type, callback):
        """Bind an event handler to a specific event type"""
        self.handlers[event_type] = callback
    
    def select(self):
        """Called when the widget is selected/focused"""
        self.selected = True

    def deselect(self):
        """Called when the widget is deselected/unfocused"""
        self.selected = False