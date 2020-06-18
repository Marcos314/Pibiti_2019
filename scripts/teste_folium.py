import numpy as np
import pandas as pd

# For plotting maps
import folium

from folium import Figure
from folium.plugins import TimeSliderChoropleth

# For Regular Expressions
import re

# For working with geographical data
import geopandas as gpd

# For plotting in python
import matplotlib
import matplotlib.pyplot as plt


df = pd.read_csv('/home/marcos/Desktop/dados/clean_data/newdataset.csv')

df['ANO']=(df['ANO'].astype(int)
covid_dict={}
for i in df['state_id'].unique():
    covid_dict[i]={}
    for j in df[df['state_id']==i].set_index(['state_id']).values:   
        covid_dict[i][j[0]]={'color':j[1],'opacity':0.7}


geodata = gpd.read_file('/home/marcos/Desktop/dados/analise/my_d3geojson.geojson')

#print(geodata.head())

fig6=Figure(height=850,width=1000)
m6 = folium.Map([24, 84], tiles='cartodbpositron', zoom_start=5)
fig6.add_child(m6)

g = TimeSliderChoropleth(
    geodata.set_index('ANO').to_json(),
    styledict=covid_dict
).add_to(m6)
m6
