from axto.core import Engine
from axto.widgets.box import Box
from axto.widgets.label import Label
from axto.widgets.input import Input


def main():
    app = Engine()

    label = Input(2, 2, 20, placeholder="Type something...")
    app.add_widget(label)
    
    app.run()

if __name__ == "__main__":
    main()