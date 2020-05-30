#Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Obtendo dataframe

df = pd.read_csv('/home/marcos/Desktop/dados/analise/pagamentosAtrasadosCidade.csv')

#DashBoard para mostrar tabela
def generate_table(dataframe, max_rows=8):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),

        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# app.layout = html.Div(children=[
#     html.H1(children='Quantidade de beneficios em atraso por cidade'),
#     generate_table(df)
# ])

#Visualização do dataframe em gráfico de dispersão

app.layout =  html.Div([
    
    html.Div(   
        className="banner",
        children=[
            html.H6("PIBITI 2019"),
            html.Img(id="logo1", src=app.get_asset_url("bf2.png")),
            html.Img(src=app.get_asset_url("ifgformosa2015resumida01.jpg"))
        ],
    ),

    html.Div([
        
        html.H2('DADOS BOLSA FAMÍLIA 2013 - 2019')
    ]),
        
    html.Div([
        dcc.Graph(
            id='qtd_atraso',
            figure={
                'data': [
                    dict(
                        x = df[df['NOME_MUNICIPIO'] == i]['MES_COMPETENCIA'],
                        y = df[df['NOME_MUNICIPIO'] == i]['MES_COMPETENCIA'],
                        text = df[df['NOME_MUNICIPIO'] == i]['NOME_MUNICIPIO'],
                        mode = 'markers',
                        opacity = 0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=i
                    ) for i in df.NOME_MUNICIPIO.unique()
                ],
                'layout': dict(
                    xaxis={'type': 'log', 'title': 'QTD em atraso'},
                    yaxis={'title': 'QTD em atraso'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ]),


    html.Div([
        html.H3('Quantidade de beneficios em atraso por cidade', id='title'),
        generate_table(df)
    ]),

    
    html.Div(

        id="div3",
        children=[
            html.H3('Mapa com valores médios por cidade')
        ]
        
        
    ) 
])
    


if __name__ == '__main__':
    app.run_server(debug=True)

#app.run_server(debug = True, port=8053)