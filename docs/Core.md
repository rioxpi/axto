# CORE

1. Hello world example

```Python
from axto.core import Engine
from axto.widgets.box import Box

app = Engine()
box1 = Box(x=5, y=5, width=20, height=10)
box2 = Box(x=30, y=5, width=20, height=10, border_style="double")
app.add_widget(box1)
app.add_widget(box2)
app.run()
```

1. `from axto.core import Engine` <- Imports main engine
2. `from axto.widgets.box import Box` <- Imports simple widget
3. `app.add_widget(box1)` <- Adds widget to Engine
4. `app.run()` <- runs engine in raw mode

## Docs

1. Engine functions
    1. `add_widget(widget)` <- Adds widget 
    2. `run()` <- runs engine
    3. `dispatch_main_thread(func, args, kwargs)` <- Executes safe function from thread