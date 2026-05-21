from axto.core import Engine
from axto.widgets.label import Label

def main():
    app = Engine()

    label = Label(5, 5, "Hello, World!", "73")
    app.add_widget(label)
    
    
    app.run()

if __name__ == "__main__":
    main()