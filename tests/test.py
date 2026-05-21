from axto.core import Engine
from axto.widgets.box import Box
from axto.widgets.label import Label
from axto.widgets.input import Input
from axto.widgets.button import Button

def main():
    app = Engine()

    box = Box(2, 2, 30, 10, border_style="bold")
    app.add_widget(box)

    button = Button(5, 5, "Click Me")
    app.add_widget(button)

    app.run()

if __name__ == "__main__":
    main()