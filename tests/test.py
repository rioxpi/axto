from axto import Engine
from axto.widgets.box import Box

def test_engine():
    engine = Engine()
    box1 = Box(5, 5, 20, 10, default_color="37", selected_color="32", border_style="single")
    box2 = Box(30, 5, 20, 10, default_color="37", selected_color="32", border_style="double")
    
    box2.bind("key", lambda key: print(f"Box 2 received key: {key}"))
    
    engine.add_widget(box1)
    engine.add_widget(box2)
    
    # Run the engine (this will block until you exit)
    engine.run()

if __name__ == "__main__":
    test_engine()