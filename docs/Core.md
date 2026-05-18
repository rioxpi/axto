# CORE
1. Hello world example
```
from axto.core import Engine

from axto.widgets.box import Box

  

app = Engine()

box1 = Box(x=5, y=5, width=20, height=10)

box2 = Box(x=30, y=5, width=20, height=10, border_style="double")

app.add_widget(box1)

app.add_widget(box2)

app.run()
```
2. `from axto.core import Engine` <- Imports main engine
3. `from axto.widgets.box import Box` <- Imports simple widget
4. `app.add_widget(box1)` <- Adds widget to Engine
5. `app.run` <- runs engine in raw mode 