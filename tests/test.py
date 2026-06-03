"""
WARNING: This file is only used to testing features.
"""

from axto.core import Engine
from axto.widgets.progress_bar import ProgressBar
from axto.widgets.label import Label
from axto.widgets.box import Box
from axto.widgets.input import Input
import sys
from axto.styles import Color

def main():
    app = Engine()


    app.set_min_size(80, 24)
    
    lb = Label(10,10,"HELLO")
    
    bx = Box(0,0,1.0,1.0)
    
    inpt = Input(10,20,50)
    
    app.theme.border_focus = Color.RED
    
    inpt.bind("submit", lambda val: sys.exit())
    
    
    app.add_widget(bx)

    app.add_widget(inpt)

    
    pg = ProgressBar(5,5,50)
    app.add_widget(lb)
    pg.set_progress(0.5)
    app.add_widget(pg)
    
    app.run()
    

if __name__ == "__main__":
    main()