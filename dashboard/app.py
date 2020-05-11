import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

df = pd.read_csv('/home/marcos/Desktop/df_teste.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(max(len(dataframe), max_rows))
        ])
    ])

############################ PLOTAGEM DE GRÁFICOS #############################

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig = px.bar(df,x='ANO',y='VALORES')

app.layout = html.Div(children=[

    html.H2(children='Dashboard'),

    html.Div([    
    dcc.Graph(
        figure=fig,
        'layout': {
                'title': 'Dash Data Visualization'
            }
        
        
    ),
    
    html.H4(children='DF TESTE'),
    generate_table(df)
    
    

    ])
    
])


if __name__ == '__main__':
    app.run_server(debug=True)