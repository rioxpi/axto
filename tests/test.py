from axto.core import Engine
from axto.widgets.scroll_list import ScrollList
from axto.widgets.box import Box
from axto.widgets.label import Label

def main():
    app = Engine()

    main_box = Box(1, 1, 1.0, 1.0)  # Full screen box
    app.add_widget(main_box)
    
    header_label = Label(0.5, 2, 'WELCOME TO AXTO')
    app.add_widget(header_label)
        
    #scroll_list = ScrollList(2, 2, 30, 3, items=["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"])
    #app.add_widget(scroll_list)

    app.run()

if __name__ == "__main__":
    main()