"""
WARNING: This file is only used to testing features.
"""

from axto.core import Engine
from axto.widgets import *
from axto.styles import Color
from axto.scene import Scene
from axto.scene_manager import SceneManager

def main():
    app = Engine()

    app.add_popup("HELLO", "WELCOME IN MY WORLD")
            
    app.run()
    

if __name__ == "__main__":
    main()