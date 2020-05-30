import pandas as pd
import plotly.express as px

df = pd.read_csv('/home/marcos/Desktop/dados/clean_data/datasetCompleto2.csv')

print(df.head())

# fig = px.scatter(df,x='total_bill', y='tip', title='TESTE')

# fig.show()