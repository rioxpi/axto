from .widgets.box import Box
from .widgets.label import Label
from .terminal import Terminal
from .scene import Scene
from .scene_manager import SceneManager

class DefaultScenes:
    def __init__(self, app):
        self.app = app
        self.scene_manager = SceneManager(app)
    
    def construct_terminal_too_small(self, min_size: tuple):
        Terminal.clear_screen()
        scene = Scene()
        box1 = Box(0, 0, 1.0, 1.0)
        label1 = Label(0.5, 0.5, f"Terminal size is too small to run (min {min_size[0]}x{min_size[1]})", align="center")
        scene.add_widget(box1)
        scene.add_widget(label1)
        self.scene_manager.add_scene("terminal_too_small", scene)
    
    def change_scene(self, name: str):
        self.scene_manager.switch_scene(name)