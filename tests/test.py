"""
WARNING: This file is only used to testing features.
"""

from axto.core import Engine
from axto.widgets import *
from axto.styles import Color
from axto.scene import Scene
from axto.scene_manager import SceneManager
from axto.widgets.tab import Tab, TabScene
from axto.keys import Key

def main():
    app = Engine()
    

    tab1 = TabScene()
    tab2 = TabScene()
    
    tab1.add_widget(Label(10,10,"SCENE 1"))
    tab2.add_widget(Button(10,10,'SCENE 2'))
    
    st = StatusBar({"1" : "tab 1", "2" : "tab 2", "ESC" : "exit"})
    
    tab1.add_widget(st)
    tab2.add_widget(st)
    
    app.add_tab('test 1', tab1, '1')
    app.add_tab('test 2', tab2, '2')
    
    app.run()
    

if __name__ == "__main__":
    main()