# WIDGETS
## BOX
1. `from axto.widgets.box import Box`
2. parameters
	1. x <- number of columns
	2. y <- number of rows
	3. width <- width in columns 
	4. high <- high in rows
	5. default_color <- drawing color
	6. selected_color <- color when focused
	7. border_style <- style of box's border ('single", 'double", 'none" )
3. Functions
	1. `bind(event_type, callback)`
		1. Currently only available event_type = "key" 
		2. example: `box.bind("key", lambda key: print(f"Box 2 received key: {key}")`