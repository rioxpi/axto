# Axto Framework Documentation

Axto is a modular, Terminal User Interface (TUI) framework designed for building scalable and interactive console applications.

## Quick Start

Below is a basic example of initializing the engine and adding widgets to the screen.

```python
from axto.core import Engine
from axto.widgets.box import Box

app = Engine()
box1 = Box(x=5, y=5, width=20, height=10)
box2 = Box(x=30, y=5, width=20, height=10, border_style="double")
app.add_widget(box1)
app.add_widget(box2)
app.run()

```

---

## Core Engine

The `Engine` is the main loop handler and application state manager.

### Engine Properties

| Property | Type | Description |
| --- | --- | --- |
| `theme` | `Theme` | Manages and sets widget themes. |
| `min_size` | `tuple` | Sets the minimal allowed size of the terminal window. |

### Engine Methods

| Method | Arguments | Description |
| --- | --- | --- |
| `add_widget` | `widget` | Adds a root widget or container to the engine. |
| `run` | None | Runs the engine in raw mode. |
| `dispatch_main_thread` | `func`, `args`, `kwargs` | Safely executes a function from a background thread. |
| `add_tab` | `title`, `scene`, `key` | Adds a new tab requiring a `TabScene` and an activation key. |
| `add_popup` | `title`, `message`, `duration` | Displays a temporary popup; duration defaults to 3.0 seconds. |

---

## Scene Management

Scenes allow you to switch between different UI panels seamlessly.

### Scene

Imported via `from axto.scene import Scene`.

| Method | Arguments | Description |
| --- | --- | --- |
| `add_widget` | `widget` | Adds a widget to the scene and returns its instance (e.g., `scene.add_widget(Button(5,6, "START"))`). |

### SceneManager

Imported via `from axto.scene_manager import SceneManager`. It requires the `engine` instance parameter during initialization.

| Method | Arguments | Description |
| --- | --- | --- |
| `add_scene` | `name`, `scene` | Registers a scene in the manager under a unique string name. |
| `switch_scene` | `name` | Hides the current scene, triggers deselect events, and activates the targeted scene. |
