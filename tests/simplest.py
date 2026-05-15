from axto import Engine
from axto.widgets.box import Box

app = Engine()
box1 = Box(x=5, y=5, width=20, height=10)
app.add_widget(box1)
app.run()