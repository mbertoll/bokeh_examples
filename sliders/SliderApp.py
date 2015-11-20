"""
This file demonstrates a bokeh server application, which you can
run with `bokeh serve sliders_app.py`
"""

import numpy as np

from bokeh.plotting import Figure
from bokeh.models import Plot, ColumnDataSource
from bokeh.models.widgets import HBox, Slider, TextInput, VBoxForm
from bokeh.io import curdoc


class SliderApp:
    def __init__(self):
        # Set up data
        self.N = 200
        x = np.linspace(0, 4*np.pi, self.N)
        y = np.sin(x)
        self.source = ColumnDataSource(data=dict(x=x, y=y))


        # Set up plot
        self.plot = Figure(plot_height=400, plot_width=400, title="my sine wave",
                           tools="crosshair,pan,reset,resize,save,wheel_zoom",
                           x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

        self.plot.line('x', 'y', source=self.source, line_width=3, line_alpha=0.6)


        # Set up widgets
        self.text = TextInput(title="title", name='title', value='my sine wave')

        self.offset = Slider(title="offset", name='offset',
                        value=0.0, start=-5.0, end=5.0, step=0.1)

        self.amplitude = Slider(title="amplitude", name='amplitude',
                           value=1.0, start=-5.0, end=5.0)

        self.phase = Slider(title="phase", name='phase',
                       value=0.0, start=0.0, end=2*np.pi)

        self.freq = Slider(title="frequency", name='frequency',
                      value=1.0, start=0.1, end=5.1)

        self.text.on_change('value', self.update_title)
        for w in [self.offset, self.amplitude, self.phase, self.freq]:
            w.on_change('value', self.update_data)

    def get_app(self):
        # Set up layouts and add to document
        inputs = VBoxForm(children=[self.text, self.offset, self.amplitude, self.phase, self.freq])

        hbox = HBox(children=[inputs, self.plot])

        return hbox    

    # Set up callbacks
    def update_title(self, attrname, old, new):
        self.plot.title = self.text.value
        
    def update_data(self, attrname, old, new):

        # Get the current slider values
        a = self.amplitude.value
        b = self.offset.value
        w = self.phase.value
        k = self.freq.value

        # Generate the new curve
        x = np.linspace(0, 4*np.pi, self.N)
        y = a*np.sin(k*x + w) + b

        self.source.data = dict(x=x, y=y)

# Uncomment to run with bokeh serve SliderApp.py
#app = SliderApp()
#hbox = app.get_app()
#curdoc().add(hbox)
