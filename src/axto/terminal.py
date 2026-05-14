import sys

class Terminal:
    # ANSI escape codes for terminal control
    CLEAR = "\033[2J"
    HOME = "\033[H"
    RESET = "\033[0m"

    @staticmethod
    def move_cursor(x, y):
        # ANSI uses format: \033[y;xH (first row, then column)
        sys.stdout.write(f"\033[{y};{x}H")

    @staticmethod
    def clear_screen():
        sys.stdout.write(Terminal.CLEAR + Terminal.HOME)
        sys.stdout.flush()

    @staticmethod
    def write(text, color_code=None):
        if color_code:
            sys.stdout.write(f"\033[{color_code}m{text}{Terminal.RESET}")
        else:
            sys.stdout.write(text)
        sys.stdout.flush()