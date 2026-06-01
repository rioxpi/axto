from axto.core import Engine
from axto.widgets.progress_bar import ProgressBar
from axto.widgets.label import Label

def main():
    app = Engine()

    lb = Label(10,10,"HELLO")
    
    pg = ProgressBar(5,5,50)
    app.add_widget(lb)
    pg.set_progress(0.5)
    app.add_widget(pg)
    
    app.run()
    

if __name__ == "__main__":
    main()