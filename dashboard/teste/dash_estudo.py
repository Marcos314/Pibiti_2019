import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
# To display the figure defined by this dict, use the low-level plotly.io.show function
import plotly.io as pio

#Figuras como dicionários

fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
})



pio.show(fig)