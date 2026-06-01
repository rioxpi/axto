from axto.scene import Scene
from axto.core import Engine
from axto.terminal import Terminal

class SceneManager:
    """
    Manages multiple scenes.
    """
    def __init__(self, engine: Engine) -> None:
        self.engine = engine
        self.scenes = {}
        self.current_scene = None
    
    def add_scene(self, name: str, scene: Scene) -> None:
        """Add a scene to the manager

        Args:
            name (str): The name of the scene
            scene (Scene): The scene instance to add
        """
        self.scenes[name] = scene
    
    def switch_scene(self, name: str) -> None:
        """Switch to a different scene

        Args:
            name (str): The name of the scene to switch to
        """
        if name not in self.scenes:
            raise ValueError(f"Scene '{name}' does not exist.")
        
        if self.engine.widgets and self.engine.focus_index < len(self.engine.widgets):
            self.engine.widgets[self.engine.focus_index].deselect()
        
        for w in self.scenes[name].widgets:
            w.engine = self.engine
        
        self.engine.widgets = self.scenes[name].widgets
        self.engine.focus_index = 0  # Reset focus to the first widget
        self.current_scene = name
        
        if self.engine.widgets:
            self.engine.widgets[0].select()  # Select the first widget in the new scene
        
        Terminal.clear_screen()
        Engine._render_all_widgets(self.engine)