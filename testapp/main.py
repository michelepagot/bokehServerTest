import numpy as np

from bokeh.models import Button, Dropdown
from bokeh.plotting import figure, curdoc, vplot


# create a plot and style its properties
p = figure(x_range=(0, 100), y_range=(0, 100), toolbar_location=None)
p.border_fill_color = 'grey'
p.background_fill_color = 'white'
p.outline_line_color = None
p.grid.grid_line_color = None

i = 0
circle_color = "olive"

# add a text renderer to out plot (no data yet)
r = p.text(x=[], y=[], text=[], text_color=[], text_font_size="20pt",
           text_baseline="middle", text_align="center")

ds = r.data_source

# create a callback that will add a number in a random location
def callbackButton():
    global i
    global circle_color
    ds.data['x'].append(np.random.random() * 70 + 15)
    ds.data['y'].append(np.random.random() * 70 + 15)
    ds.data['text_color'].append(circle_color)
    ds.data['text'].append(str(i))
    ds.trigger('data', ds.data, ds.data)
    i = i + 1

def callbackSelect(color_in):
    global circle_color
    circle_color = color_in


# add a button widget and configure with the call back
button = Button(label="Add Random Data")
select = Dropdown(menu=[('Black','black'),('Green','green'),('Blue','blue'),None,('Red','red')],default_value='red')

button.on_click(callbackButton)
select.on_click(callbackSelect)

# put the button and plot in a layout and add to the document
curdoc().add_root(vplot(button,select, p))