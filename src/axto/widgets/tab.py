from .base import Widget
from axto.scene import Scene
from axto.keys import Key
from axto.scene_manager import SceneManager

class TabScene(Scene):
    def __init__(self) -> None:
        super().__init__()

class Tab(Widget):
    def __init__(self, engine):
        super().__init__(0, 0, 1.0, 1, selectable=False)
        self.tabs = []
        self.scene_manager = SceneManager(engine=engine)
        self.selected_tab_index = 0

    def add_tab(self, title: str, contents: TabScene, activation_key: Key | str):
        self.tabs.append({
            "title": title,
            "activation_key": activation_key,
        })
                
        scene_name = f"scene_data_{title}"
        self.scene_manager.add_scene(scene_name, contents)
        
        if len(self.tabs) == 1:
            self.scene_manager.switch_scene(scene_name)

    def on_key(self, key: Key) -> None:
        for idx, t in enumerate(self.tabs):
            if t['activation_key'] == key:
                self.scene_manager.switch_scene(f"scene_data_{t['title']}")
                self.selected_tab_index = idx

    def draw(self, term) -> None:
        current_x = self.x
        
        for idx, tab in enumerate(self.tabs):
            color = self.theme.widget_selected if self.selected_tab_index == idx else self.theme.widget_deselected
            
            data = f" < {tab['title']} > "
            
            term.move_cursor(x=current_x, y=self.y)
            term.write(data, color)
            
            current_x += len(data) + 2