import sys
import tty
import termios

class Engine:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        # Add switching to raw mode for terminal input
        pass

    def stop(self):
        self.running = False