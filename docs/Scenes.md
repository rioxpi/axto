# Scenes

1. You can switch between different UI panels, it is optional

## SCENE

1. `from axto.scene import Scene`
2. Parameters
	1. None
3. Functions
	1. `add_widget(widget)`
		1. Adds a widget  to the scene and returns its instance
		2. Example: `button_scene = scene.add_widget(Button(5,6, "START"))`

## SCENE MANAGER

1. `from axto.scene_manager import SceneManager`
2. Parameters
	1. `engine` <- instance of main Engine
3. Functions
	1.  `add_scene(name, scene)`
		1. Registers a scene in the manager under a unique name 
		2. Example: `manager.add_scene("menu", manu_scene)`
	2. `switch_scene`
		1. Hides the current scene (triggering deselect) and activates the new one 
		2. Example: `manager.switch_scene("menu")`