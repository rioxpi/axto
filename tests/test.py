from axto.core import Engine
from axto.widgets.scroll_list import ScrollList

def main():
    app = Engine()

    scroll_list = ScrollList(2, 2, 30, 3, items=["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"])
    app.add_widget(scroll_list)

    app.run()

if __name__ == "__main__":
    main()