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

    scene_manager = SceneManager(app)
    
    scene = Scene()
    
    ctn = Container(10, 10, 100, 100, title="OPTIONS")
    
    cb1 = ctn.add_child(Button(0,0,"HELLO"))
    cb2 = ctn.add_child(CheckBox(5,5,"LIKE ME?"))
    
    scene.add_widget(ctn)
    
    scene_manager.add_scene("test", scene)

    scene_manager.switch_scene("test")
    scene2 = Scene()
    scene2.add_widget(Button(0,0,"TEST"))
    
    scene_manager.add_scene("test2", scene2)
    
    scene_manager.switch_scene("test2")
        
    app.run()
    

if __name__ == "__main__":
    main()