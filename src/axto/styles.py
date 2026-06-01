class Color:
    RESET = "0"
    
    BOLD = "1"
    DIM = "2"
    UNDERLINE = "4"
    
    BLACK = "30"
    RED = "31"
    GREEN = "32"
    YELLOW = "33"
    BLUE = "34"
    MAGENTA = "35"
    CYAN = "36"
    WHITE = "37"
    
    BRIGHT_BLACK = "90"
    BRIGHT_RED = "91"
    BRIGHT_GREEN = "92"
    BRIGHT_YELLOW = "93"
    BRIGHT_BLUE = "94"
    BRIGHT_MAGENTA = "95"
    BRIGHT_CYAN = "96"
    BRIGHT_WHITE = "97"

class Theme:
    def __init__(self) -> None:
        self.default_text = Color.WHITE
        self.border_normal = Color.BRIGHT_BLACK
        self.border_focus = Color.GREEN
        
        self.widget_selected =  Color.BOLD + ";" + Color.GREEN    # Pogrubiony zielony
        self.widget_deselected = Color.WHITE
        self.placeholder = Color.DIM + ";" + Color.WHITE
        
        self.progress_fill = Color.CYAN
        self.progress_complete = Color.GREEN
        
        self.list_item_selected = "1;" + Color.GREEN
        self.list_item_normal = Color.WHITE