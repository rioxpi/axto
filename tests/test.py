from axto.core import Engine
from axto.widgets.box import Box
from axto.widgets.button import Button
from axto.widgets.input import Input
from axto.scene_manager import SceneManager
from axto.scene import Scene

def main():
    app = Engine()
    manager = SceneManager(app)

    # Main menu scene
    menu_scene = Scene()
    menu_scene.add_widget(Box(2, 2, 30, 8))
    
    btn_start = menu_scene.add_widget(Button(5, 4, "START GAME"))
    btn_settings = menu_scene.add_widget(Button(5, 6, "SETTINGS"))

    # Actions for buttons
    btn_settings.bind("press", lambda: manager.switch_scene("settings"))

    # Settings scene
    settings_scene = Scene()
    settings_scene.add_widget(Box(2, 2, 45, 8))
    
    # Input for player nickname
    settings_scene.add_widget(Input(5, 4, 20, placeholder="Enter nickname..."))
    
    btn_back = settings_scene.add_widget(Button(5, 6, "BACK TO MENU"))
    
    # Action: Return to main menu
    btn_back.bind("press", lambda: manager.switch_scene("menu"))


    manager.add_scene("menu", menu_scene)
    manager.add_scene("settings", settings_scene)

    # Start with the main menu
    manager.switch_scene("menu")
    app.run()

if __name__ == "__main__":
    main()