# WIDGETS

## BOX
1. `from axto.widgets.box import Box`
2. parameters
	1. x <- number of columns
	2. y <- number of rows
	3. width <- width in columns
	4. height <- height in rows
	5. default_color <- drawing color
	6. selected_color <- color when focused
	7. border_style <- style of box's border ("single", "double", "rounded", "bold", "none")
	8. bg_color <- background color
	9. selectable <- can be selected
3. Functions
	1. `bind(event_type, callback)`
		1. available: "key" (pressing any key), "select", "deselect"
		2. example: `box_widget.bind("key", lambda key: print(f"Box 2 received key: {key}"))`

## BUTTON

1. `from axto.widgets.button import Button`
2. parameters
	1. x <- number of columns
	2. y <- number of rows
	3. text <- text showed in button
	4. selectable <- can be selected
3. Functions
	1. `bind(event_type, callback)`
		1. available: "key" (pressing any key), "select", "deselect", "press" (button has been pressed)
		2. example: `button_widget.bind("press", lambda press: print(f"Button has been pressed"))`
		

## INPUT
1. `from axto.widgets.input import Input`
2. parameters
	1. x <- number of columns
	2. y <- number of rows
	3. width <- width in columns
	4. placeholder <- text showed when nothing is in the box
	5. selectable <- can be selected
3. Functions
	1. `bind(event_type, callback)`
		1. available event_types: "key" (pressing any key), "select", "deselect", "submit" (ENTER was pressed on input)
		2. example: `input_widget.bind("submit", lambda text: print(f"Input submitted: {text}")`

## LABEL
1. `from axto.widgets.label import Label`
2. parameters
	1. x <- number of columns
	2. y <- number of rows
	3. width <- width in columns
	4. text <- text in label
	5. align <- left, center, right
	6. color <- text color
3. Functions
	1. `set_text(text, resize=True)`
		1. text <- the new string to display 
		2. resize <- changing width, useful when preset width
		3. example: `label_widget.set_text("Hello World!", resize=False)`
