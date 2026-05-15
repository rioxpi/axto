# AXTO

1. Simple TUI library

## INSTALATION
1. `pip install axto`

## QUICK START
```
from axto import Engine
from axto.widgets.box import Box

app = Engine()
box1 = Box(x=5, y=5, width=20, height=10)
app.add_widget(box1)
app.run()
```

## AVAIABLE WIDGETS
1. BOX

## Control
1. `q` - exit engine
2. `TAB` - select next widget