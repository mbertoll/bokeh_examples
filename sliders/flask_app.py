from flask import render_template, Flask

from SliderApp import SliderApp

from bokeh.embed import autoload_server
from bokeh.client import push_session
from bokeh.io import curdoc
from bokeh.resources import Resources

app = Flask(__name__)

@app.route('/')
def index():
    applet = SliderApp()
    layout = applet.get_app()
    doc = curdoc().add(layout)
    push_session(curdoc())

    tag = autoload_server(layout, loglevel='debug')

    return render_template('slider_app.html', tag=tag)


if __name__ == '__main__':
    print("STARTED")
    app.run(debug=True)
