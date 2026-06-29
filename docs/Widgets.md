# Widgets

All UI components inherit from the main `Widget` base class.

## Base Widget Properties & Methods

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `int` | `float` | X-axis coordinate. Use `int` for absolute columns or `float` for screen percentage. |
| `y` | `int` | `float` | Y-axis coordinate. Use `int` for absolute rows or `float` for screen percentage. |
| `width` | `int` | `float` | Component width. Use `int` for absolute columns or `float` for screen percentage. |
| `height` | `int` | `float` | Component height. Use `int` for absolute rows or `float` for screen percentage. |
| `selectable` | `bool` | Determines if the widget can receive focus. |

**Base Methods:**

* `bind(event_type, callback)`: Attaches a callback function to specific widget events. Available global events include `"key"`, `"select"`, and `"deselect"`.

### Available Components

Below is the list of available widgets and their unique parameters or events.

### Box

*Import:* `from axto.widgets import Box`

* **`default_color`** (`str`): Standard drawing color.
* **`selected_color`** (`str`): Color applied when focused.
* **`border_style`** (`str`): Options include `"single"`, `"double"`, `"rounded"`, `"bold"`, or `"none"`.
* **`bg_color`** (`str`): Background color of the box.

### Button

*Import:* `from axto.widgets import Button`

* **`text`** (`str`): Text displayed on the button.
* **Event `press`**: Triggered when the button is actively pressed.

### Input

*Import:* `from axto.widgets import Input`
 
* **`placeholder`** (`str`): Text shown when the input box is empty.
* **`allow_to_submit_on_exit`** (`bool`): Submits current text upon losing focus.
* **`default_text`** (`str`): Pre-filled text within the input.
* **`allow_blank_string`** (`bool`): Permits submitting empty strings.
* **Event `submit`**: Triggered when the ENTER key is pressed.

### Label

*Import:* `from axto.widgets import Label`

* **`text`** (`str`): The string to display.
* **`align`** (`str`): Text alignment option (`"left"`, `"center"`, `"right"`).
* **`color`** (`str`): Text color.
* **Method `set_text(text, resize=True)`**: Updates the displayed text and dynamically adjusts widget width if `resize` is true.

### ScrollList

*Import:* `from axto.widgets import ScrollList`

* **`items`** (`list`): A list of items to display in the scrollable view.

### ProgressBar

*Import:* `from axto.widgets import ProgressBar`

* **`placeholder`** (`str`): Text displayed inside the progress bar.
* **Method `set_progress(value)`**: Updates the completion state using a float value between 0.0 and 1.0.

### Select

*Import:* `from axto.widgets import Select`

* **`options`** (`list`): List of available options.
* **`default_index`** (`int`): Initially selected item index.
* **`label`** (`str`): Text displayed preceding the selector.
* **Event `change`**: Triggered upon arrow key navigation; passes both value and index.

### Container

*Import:* `from axto.widgets import Container`

* **`has_border`** (`bool`): Determines if a border is drawn around the container.
* **`title`** (`str`): Top-aligned title text.
* **Method `add_child(widget)`**: Nests a widget within the container.

### StatusBar

*Import:* `from axto.widgets import StatusBar`

* **`shortcuts`** (`dict[str, str]`): A dictionary mapping shortcut keys to descriptions.

---

## Styling and Themes

Colors and theme properties are managed via `from axto.styles import Color`.

### Available Colors and Modifiers

| Category | Options |
| --- | --- |
| Standard Colors | `BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`. |
| Bright Colors | `BRIGHT_BLACK`, `BRIGHT_RED`, `BRIGHT_GREEN`, `BRIGHT_YELLOW`, `BRIGHT_BLUE`, `BRIGHT_MAGENTA`, `BRIGHT_CYAN`, `BRIGHT_WHITE`. |
| Text Modifiers | `BOLD`, `DIM`, `UNDERLINE`. |

### Theme Set Variables

Customize the framework's visual behavior by modifying these predefined theme attributes:

* **`default_text`**: Used for standard text rendering.
* **`border_normal`**: Default border color for boxes.
* **`border_focus`**: Border color when a box is actively selected.
* **`widget_selected`**: Applied when an interactive widget is focused.
* **`widget_deselected`**: Applied when an interactive widget is in a normal state.
* **`placeholder`**: Color for input placeholder text.
* **`progress_fill`**: Color applied to the incomplete portion of a progress bar.
* **`progress_complete`**: Color applied to the completed portion of a progress bar.
* **`list_item_selected`**: Highlight color for the focused item in a ScrollList.
* **`list_item_normal`**: Default color for unfocused items in a ScrollList.