# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import webbrowser
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
# bar mode type: ['stack', 'group', 'overlay', 'relative']

app.layout = html.Div(children=[
    html.H1(children='Número de caixas vendidas de acordo com cada fruta.'),

    html.Div(children='''
        Utilizamos esses dados para sabermos onde cada fruta vende mais em cada cidade
    '''),

    dcc.Graph(
        id='Grafico',
        figure=fig
    )
])

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/')
    app.run_server(debug=True)
