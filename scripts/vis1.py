# basic modules 
import geopandas as gpd
import pandas as pd 
import json 
import glob 
import os 
# visualizaztion modules 
from bokeh.resources import INLINE 
from bokeh.io import output_notebook, show, output_file 
from bokeh.plotting import figure, save 
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar 
from bokeh.palettes import brewer,mpl 
# interactive visualization models 
from bokeh.io import curdoc, output_notebook 
from bokeh.models import Slider, HoverTool 
from bokeh.layouts import widgetbox, row, column



df = pd.read_csv('/home/marcos/Desktop/dados/dadosVis/df1.csv')
df.groupby('NOME_MUNICIPIO').head(21)

#Lendo os arquivos shp
gdf = gpd.read_file('/home/marcos/Desktop/dados/ride_shp/rideTotal2.shp')

#RASCUNHO
def json_data(selectYear):
    ano = selectYear
    dfYear = df[df['MES_REFERENCIA'] == ano]
    merged = gdf.merge(dfYear, left_on ='NM_MUNICIP', right_on ='NOME_MUNICIPIO', how ='left')
    merged['Valor'] = merged.VALOR_PARCELA.fillna("N/A")
    del merged['NOME_MUNICIPIO']
    del merged['VALOR_PARCELA']
    merged = merged.groupby('NM_MUNICIP').head(1)
    merged_json = json.loads(merged.to_json())
    json_data = json.dumps(merged_json)
    return merged

#json_data(201612)


# Função para retornar um json
def json_data(selectYear):
    ano = selectYear
    dfYear = df[df['MES_REFERENCIA'] == ano]
    merged = gdf.merge(dfYear, left_on ='NM_MUNICIP', right_on ='NOME_MUNICIPIO', how ='left')
    merged['Valor'] = merged.VALOR_PARCELA.fillna("N/A")
    del merged['NOME_MUNICIPIO']
    del merged['VALOR_PARCELA']
    merged_json = json.loads(merged.to_json())
    json_data = json.dumps(merged_json)
    return json_data

#json_data(201301)

# Input GeoJSON source that contains features for plotting.
# Select a default year to show on first display.
geosource = GeoJSONDataSource(geojson = json_data(201601))

# Define a sequential multi-hue color palette.
# I chose the Plasma theme because 10 would map to yellow :)
palette = mpl['Plasma'][10]

# Instantiate LinearColorMapper that maps numbers to a sequence of colors.
color_mapper = LinearColorMapper(palette = palette, low = 100, high = 250)

# Add the hovering tooltips.
hover = HoverTool(tooltips = [ ('Cidade','@NM_MUNICIP'),('Valor', '@Valor')])

# Create the color bar. 
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=10,width = 500, height = 20, border_line_color=None,location = (0,0), orientation = 'horizontal')

# Create the figure object.
p = figure(title = 'Valor médio do benefício por cidade da RIDE', plot_height = 600 , plot_width = 950, toolbar_location = None, tools = [hover])
# Remove the grid lines. 
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
# Increase the title font size.
p.title.text_font_size = '12pt'

# Add the patch renderer to the figure. 
# Notice that this is where you provide the Score column from the json_data and the color mapper.
p.patches('xs','ys', source = geosource,fill_color = {'field' :'Valor', 'transform' : color_mapper}, line_color = 'white', line_width = 0.5, fill_alpha =1)

# Place the color bar below the map.
p.add_layout(color_bar, 'below')

# Define the callback function.
# This is what will be called when the slider value changes.
def update_plot(attr, old, new):
    yr = slider.value
    new_data = json_data((yr))
    geosource.geojson = new_data
    p.title.text = 'Valor médio do benefício por cidade da RIDE' %yr
    
# Make a slider object.
slider = Slider(title = 'Year',start = 201301, end = 201901, step = 100, value = 201301)
slider.on_change('value', update_plot)

# Make a column layout of widgetbox (slider) and plot, and add it to the current document
layout = column(p,widgetbox(slider))
curdoc().add_root(layout)

# Show the figure.
output_file("map.html")
save(p)









