from axto.core import Engine
from axto.widgets.label import Label
from axto.widgets.box import Box


def main():
    app = Engine()

    label = Label(5, 5, "Hello, World!", "73")
    box = Box(5, 7, 20, 3, selectable=True)
    box2 = Box(5, 20, 20, 3, selectable=True)
    box3 = Box(20, 10, 20, 3, selectable=False)
    app.add_widget(label)
    
    app.add_widget(box)
    app.add_widget(box2)
    app.add_widget(box3)
    app.run()

if __name__ == "__main__":
    main()