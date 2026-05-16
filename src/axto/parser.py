import sys
from .keys import Key

def read_key() -> Key | str:
    """Reads a single key press and returns a Key enum or character."""
    ch = sys.stdin.read(1)
    
    # Escape sequence for arrow keys starts with '\033' (ESC)
    if ch == '\033':
        remaining = sys.stdin.read(2)
        
        # Map arrow key sequences to Key enums
        arrow_keys = {
            '[A': Key.UP,
            '[B': Key.DOWN,
            '[C': Key.RIGHT,
            '[D': Key.LEFT
        }
        return arrow_keys.get(remaining, Key.ESC)

    # Map control characters to Key enums
    control_keys = {
        '\t': Key.TAB,
        '\r': Key.ENTER,
        '\n': Key.ENTER,
        '\x7f': Key.BACKSPACE,
        '\x08': Key.BACKSPACE
    }
    
    return control_keys.get(ch, ch)
