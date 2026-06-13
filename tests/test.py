"""
WARNING: This file is only used to testing features.
"""

from axto.core import Engine
from axto.widgets import *
from axto.styles import Color

def main():
    app = Engine()

    ctn = Container(10, 10, 100, 100, title="OPTIONS")
    
    cb1 = ctn.add_child(Button(0,0,"HELLO"))
    cb2 = ctn.add_child(CheckBox(5,5,"LIKE ME?"))
    
    app.add_widget(ctn)
    
    app.run()
    

if __name__ == "__main__":
    main()