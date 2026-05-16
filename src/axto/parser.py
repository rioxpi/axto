import sys
import os
from .keys import Key

# --- WINDOWS ---
if sys.platform == 'win32':
    import msvcrt

    def read_key():
        # msvcrt.getch() getts a single byte from the console without echoing it
        ch = msvcrt.getch()
        
        # Windows uses a two-byte sequence for arrow keys: first 0x00 or 0xe0, then the actual key code
        if ch in (b'\x00', b'\xe0'):
            ch2 = msvcrt.getch() # Get the second byte of the arrow key sequence
            arrow_keys = {
                b'H': Key.UP,
                b'P': Key.DOWN,
                b'M': Key.RIGHT,
                b'K': Key.LEFT
            }
            return arrow_keys.get(ch2, Key.ESC)
            
        # Map control keys to our Key enum
        control_keys = {
            b'\t': Key.TAB,
            b'\r': Key.ENTER,
            b'\n': Key.ENTER,
            b'\x08': Key.BACKSPACE,
            b'\x1b': Key.ESC
        }
        if ch in control_keys:
            return control_keys[ch]
            
        try:
            return ch.decode('utf-8')
        except UnicodeDecodeError:
            return ''

# --- UNIX ---
else:
    import select

    def read_key():
        fd = sys.stdin.fileno()
        
        # Read a single byte from stdin
        try:
            ch = os.read(fd, 1).decode('utf-8')
        except Exception:
            return ''
            
        if ch == '\033':
            # Escape sequence: read the next two bytes to determine if it's an arrow key
            ready, _, _ = select.select([fd], [], [], 0.02)
            if ready:
                ch2 = os.read(fd, 1).decode('utf-8')
                if ch2 == '[':
                    ch3 = os.read(fd, 1).decode('utf-8')
                    arrow_keys = {
                        'A': Key.UP,
                        'B': Key.DOWN,
                        'C': Key.RIGHT,
                        'D': Key.LEFT
                    }
                    return arrow_keys.get(ch3, Key.ESC)
            # If we get here, it means we got an ESC key without a valid escape sequence
            return Key.ESC

        control_keys = {
            '\t': Key.TAB,
            '\r': Key.ENTER,
            '\n': Key.ENTER,
            '\x7f': Key.BACKSPACE,
            '\x08': Key.BACKSPACE
        }
        return control_keys.get(ch, ch)
