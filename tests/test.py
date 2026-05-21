from axto.core import Engine
from axto.widgets.box import Box
from axto.widgets.label import Label
from axto.widgets.input import Input


def main():
    app = Engine()

    label = Label(2, 2, "Hello, World!", color="34", align="center", width=20)
    
    app.add_widget(label)
    
    app.run()

if __name__ == "__main__":
    main()