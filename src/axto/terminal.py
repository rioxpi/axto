import sys
import os

class Terminal:
    """
    Class for terminal control
    """
    # ANSI escape codes for terminal control
    CLEAR = "\033[2J"
    HOME = "\033[H"
    RESET = "\033[0m"

    @staticmethod
    def move_cursor(x, y):
        """
        Move the cursor to a specific position

        Args:
            x (int): The column position
            y (int): The row position
        """
        # ANSI uses format: \033[y;xH (first row, then column)
        sys.stdout.write(f"\033[{y};{x}H")

    @staticmethod
    def clear_screen():
        """
        Clear the terminal screen
        """
        sys.stdout.write("\033[2J\033[3J\033[H")
        sys.stdout.flush()

    @staticmethod
    def write(text, color_code=None):
        """
        Write text to the terminal

        Args:
            text (str): The text to write
            color_code (int, str, optional): The ANSI color code. Defaults to None.
        """
        if color_code:
            sys.stdout.write(f"\033[{color_code}m{text}{Terminal.RESET}")
        else:
            sys.stdout.write(text)
        sys.stdout.flush()
    
    @staticmethod
    def get_size():
        """
        Get the terminal size

        Returns:
            tuple: (width, height) of the terminal
        """
        try:
            colums, rows = os.get_terminal_size()
            return colums, rows
        except OSError:
            return 80, 24  # Default size if unable to get terminal size

    @staticmethod
    def hide_cursor():
        sys.stdout.write("\033[?25l")
    
    @staticmethod
    def show_cursor():
        sys.stdout.write("\033[?25l")