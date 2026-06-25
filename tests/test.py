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

    test = Input(5,5,50,'test', allow_to_submit_on_exit=True, default_text="TEST", allow_blank_string=False)
    test.bind("submit", lambda text: print(f"submitted: {text}"))
    
    app.add_widget(test)
    
    app.add_widget(Button(10,10,'HELLO'))
        
    app.run()
    

if __name__ == "__main__":
    main()