# AXTO

Simple TUI (Text User Interface) library for Python.

## INSTALLATION

```shell
pip install axto
```

## QUICK START

```python
from axto import Engine
from axto.widgets.box import Box

app = Engine()
box1 = Box(x=5, y=5, width=20, height=10)
app.add_widget(box1)
app.run()
```

## AVAILABLE WIDGETS

1. BOX
2. INPUT
3. BUTTON
4. LABEL
5. SCROLL LIST
6. PROGRESS BAR

## CONTROLS

* `CTRL+C`, `CTRL+Q`, `ESC` – exit engine
* `TAB` – select next widget

## DOCUMENTATION

You can find the full documentation in the `docs/` directory.
