from axto import Engine
from axto.widgets.box import Box

def main():
    app = Engine()

    ANSI_RED = "31"
    ANSI_GREEN = "32"
    ANSI_YELLOW = "33"
    ANSI_BLUE = "34"

    app.add_widget(Box(x=2, y=2, width=3, height=9, default_color=ANSI_RED, selected_color=ANSI_RED))
    app.add_widget(Box(x=10, y=2, width=3, height=9, default_color=ANSI_RED, selected_color=ANSI_RED))
    app.add_widget(Box(x=5, y=2, width=5, height=2, default_color=ANSI_RED, selected_color=ANSI_RED))
    app.add_widget(Box(x=5, y=5, width=5, height=2, default_color=ANSI_RED, selected_color=ANSI_RED))

    app.add_widget(Box(x=15, y=2, width=3, height=3, default_color=ANSI_GREEN, selected_color=ANSI_GREEN))
    app.add_widget(Box(x=23, y=2, width=3, height=3, default_color=ANSI_GREEN, selected_color=ANSI_GREEN))
    app.add_widget(Box(x=18, y=5, width=5, height=3, default_color=ANSI_GREEN, selected_color=ANSI_GREEN))
    app.add_widget(Box(x=15, y=8, width=3, height=3, default_color=ANSI_GREEN, selected_color=ANSI_GREEN))
    app.add_widget(Box(x=23, y=8, width=3, height=3, default_color=ANSI_GREEN, selected_color=ANSI_GREEN))

    app.add_widget(Box(x=28, y=2, width=11, height=2, default_color=ANSI_YELLOW, selected_color=ANSI_YELLOW))
    app.add_widget(Box(x=32, y=4, width=3, height=7, default_color=ANSI_YELLOW, selected_color=ANSI_YELLOW))

    app.add_widget(Box(x=41, y=2, width=11, height=2, default_color=ANSI_BLUE, selected_color=ANSI_BLUE))
    app.add_widget(Box(x=41, y=9, width=11, height=2, default_color=ANSI_BLUE, selected_color=ANSI_BLUE))
    app.add_widget(Box(x=41, y=4, width=3, height=5, default_color=ANSI_BLUE, selected_color=ANSI_BLUE))
    app.add_widget(Box(x=49, y=4, width=3, height=5, default_color=ANSI_BLUE, selected_color=ANSI_BLUE))

    app.run()

if __name__ == "__main__":
    main()
