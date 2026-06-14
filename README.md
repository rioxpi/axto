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
5. SCROLL LIST2
6. PROGRESS BAR
7. Check Box
8. Select
9. Container

## CONTROLS

* `CTRL+C`, `CTRL+Q`, `ESC` – exit engine
* `TAB` – select next widget

## DOCUMENTATION

You can find the full documentation in the [`docs/`](https://github.com/rioxpi/axto/tree/main/docs) directory.

## CREDITS

Author: [rioxpi](https://github.com/rioxpi)

Github page: [axto](https://github.com/rioxpi/axto)