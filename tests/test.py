"""
WARNING: This file is only used to testing features.
"""

from axto.core import Engine
from axto.widgets import *
import sys
from axto.styles import Color

def main():
    app = Engine()
    
    app.theme.border_focus = Color.RED
    
    check_box_widget = CheckBox(10,10,"TEST")
    
    app.add_widget(check_box_widget)

    
    app.run()
    

if __name__ == "__main__":
    main()