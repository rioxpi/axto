"""
WARNING: This file is only used to testing features.
"""

from axto.core import Engine
from axto.widgets import *
from axto.styles import Color

def main():
    app = Engine()
    
    app.theme.border_focus = Color.RED
    
    check_box_widget = Select(10,10,20,["TEST1", "TEST2", "TEST4"])
    
    check_box_widget.bind("change", lambda val, ind: print(f"SELECTED {val}"))
    
    app.add_widget(check_box_widget)

    
    app.run()
    

if __name__ == "__main__":
    main()