from axto import Engine
from axto.widgets.button import Button

def button_pressed():
    print("\033[15;1HBUTTON PRESSED!\033[0m")  # Move cursor to line 15 and print message

def test_engine():
    engine = Engine()
    
    btn = Button(10, 5, "Click Me")
    btn.bind("press", button_pressed)
    engine.add_widget(btn)
    
    btn2 = Button(10, 7, "Exit")
    btn2.bind("press", lambda: print("\033[15;1HEXITING...\033[0m"))  # Bind exit button to stop the engine
    engine.add_widget(btn2)
    
    # Run the engine (this will block until you exit)
    engine.run()

if __name__ == "__main__":
    test_engine()