# WIDGETS

## MAIN WIDGET

1. The base class for all UI components. All widgets inherit these parameters and functions.
2. Parameters
	1. x <- number of columns			(int | float) `int` for absolute columns, `float` for percentage of screen width
	2. y <- number of rows				(int | float) `int` for absolute columns, `float` for percentage of screen height
	3. width <- width in columns		(int | float) `int` for absolute columns, `float` for percentage of screen width
	4. height <- height in rows			(int | float) `int` for absolute columns, `float` for percentage of screen height
	5. selectable <- can be selected	(bool)
3. Functions
	1. `bind(event_type, callback)`
		1. available: "key" (pressing any key), "select", "deselect"
		2. example: `box_widget.bind("key", lambda key: print(f"Box 2 received key: {key}"))`

## BOX
1. `from axto.widgets.box import Box`
2. parameters
	1. default_color <- drawing color		(str)
	2. selected_color <- color when focused	(str)
	3. border_style <- style of box's border ("single", "double", "rounded", "bold", "none")
	4. bg_color <- background color			(str)

## BUTTON

1. `from axto.widgets.button import Button`
2. parameters
	1. x <- number of columns
	2. y <- number of rows
	3. text <- text showed in button
	4. selectable <- can be selected
3. New event_type for bind - "press", executed when button is pressed
	1. Example: `button_widget.bind("press", lambda press: print(f"Button has been pressed"))`

## INPUT

1. `from axto.widgets.input import Input`
2. parameters
	1. placeholder <- text showed when nothing is in the box	(str)
3. New event_type for bind - "submit", executed when ENTER is pressed
	1. example: `input_widget.bind("submit", lambda text: print(f"Input submitted: {text}")`

## LABEL

1. `from axto.widgets.label import Label`
2. parameters
	1. text <- text in label		(str)
	2. align <- left, center, right	(str)
	3. color <- text color			(str)
3. Functions
	1. `set_text(text, resize=True)`
		1. text <- the new string to display 
		2. resize <- changing width, useful when preset width
		3. example: `label_widget.set_text("Hello World!", resize=False)`

## ScrollList

1. `from axto.widgets.scroll_list import ScrollList`
2. parameters
	1. items <- items to show in list	(list)

## ProgressBar

1. `from axto.widgets.progress_bar import ProgressBar`
2. parameters
	1. placeholder <- text in progress bar
3. Functions
	1. `set_progress(value)`
		1. value <- new progress (0.0-1.0)	(float)