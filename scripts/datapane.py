import pandas as pd
import altair as alt
import datapane
from datapane import Table, Plot, Report



df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1553600505&period2=1585222905&interval=1d&events=history')
chart = alt.Chart(df).encode(x='Date', y='High', y2='Low').mark_area(opacity=0.5).interactive()

datapane.Report(
  datapane.Table(df['High']), 
  datapane.Plot(chart)
).save(path='stocks.html')