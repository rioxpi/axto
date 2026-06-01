class Widget:
    """
    Base class for all widgets
    """
    def __init__(self, x, y, width, height, selectable=True):
        self._raw_x = x
        self._raw_y = y
        self._raw_w = width
        self._raw_h = height
        
        self.x = 1
        self.y = 1
        self.width = 1
        self.height = 1
        self.handlers = {} 
        self.selected = False
        self.is_selectable = selectable
        
        self.engine = None

    def resolve_geometry(self, parent_w: int, parent_h: int):
        # X
        if isinstance(self._raw_x, float):
            real_x = int(self._raw_x * parent_w) + 1
        elif self._raw_x < 0:
            real_x = parent_w + self._raw_x + 1
        else:
            real_x = self._raw_x
        
        # Y
        if isinstance(self._raw_y, float):
            real_y = int(self._raw_y * parent_h) + 1
        elif self._raw_y < 0:
            real_y = parent_h + self._raw_y + 1
        else:
            real_y = self._raw_y
        
        # Width
        if isinstance(self._raw_w, float):
            real_w = int(self._raw_w * parent_w)
        elif self._raw_w < 0:
            real_w = parent_w - real_x + self._raw_w + 1
        else:
            real_w = self._raw_w
        
        # Height
        if isinstance(self._raw_h, float):
            real_h = int(self._raw_h * parent_h)
        elif self._raw_h < 0:
            real_h = parent_h - real_y + self._raw_h + 1
        else:
            real_h = self._raw_h
        
        # Border adjustment
        self.x = max(1, min(real_x, parent_w))
        self.y = max(1, min(real_y, parent_h))
        
        max_allowed_w = parent_w - self.x + 1
        max_allowed_h = parent_h - self.y + 1
        self.width = max(1, min(real_w, max_allowed_w))
        self.height = max(1, min(real_h, max_allowed_h))
    
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
    
    @property
    def theme(self):
        if hasattr(self, "engine") and self.engine:
            return self.engine.theme

        from axto.styles import Theme
        return Theme()