from axto.core import Engine
from axto.widgets.box import Box

def main():
    app = Engine()
    
    box1 = Box(x=5, y=5, width=20, height=10)
    box2 = Box(x=30, y=5, width=20, height=10, border_style="double")
    app.add_widget(box1)
    app.add_widget(box2)
    
    app.run()

if __name__ == "__main__":
    main()