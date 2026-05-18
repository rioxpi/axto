from axto.core import Engine
from axto.widgets.box import Box
from axto.widgets.button import Button
from axto.scene import Scene
from axto.scene_manager import SceneManager

app = Engine()
manager = SceneManager(app)

# 1. Create Menu Scene
menu_scene = Scene()
menu_scene.add_widget(Box(2, 2, 30, 8, border_style="single"))
btn_start = menu_scene.add_widget(Button(5, 4, "START GAME"))
btn_start.bind("press", lambda: manager.switch_scene("game"))

# 2. Create Game Scene
game_scene = Scene()
game_scene.add_widget(Box(2, 2, 30, 8, border_style="double"))
btn_back = game_scene.add_widget(Button(5, 4, "BACK TO MENU"))
btn_back.bind("press", lambda: manager.switch_scene("menu"))

# 3. Registration and Start
manager.add_scene("menu", menu_scene)
manager.add_scene("game", game_scene)

manager.switch_scene("menu")
app.run()