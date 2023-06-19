from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import webbrowser

app = Dash(__name__)

dados = pd.read_excel('meuteste1.xlsx')
imagem = px.bar(dados, x='Semestres', y="Medias", color='Pessoas', barmode='group', range_color='red')
opc = list(dados['Pessoas'].unique())
opc.append('Todos os Alunos')
app.layout = html.Div(children=[
    html.H1(children='Alunos e suas notas.'),
    html.P('Escolha qual aluno quer ver: '),
    # html.P(id="output"),
    dcc.RadioItems(opc, opc[len(opc) - 1], inline=True, id='escolha'),
    # multi=True server para poder escolher nais de uma opção

    html.H2(children='Dashboard para professores.'),
    html.P(children='Veja o gráfico abaixo.'),
    dcc.Graph(
        id='grafico',
        figure=imagem
    )

])


@app.callback(
    Output('grafico', 'figure'),
    Input('escolha', 'value')
)
def update_output(teste):
    if teste == "Todos os Alunos":
        imagem = px.bar(dados, x='Semestres', y="Medias", color='Pessoas', barmode='group', range_color='red')
    else:
        tabela_filtarda = dados.loc[dados['Pessoas'] == teste, :]
        imagem = px.bar(tabela_filtarda, x='Semestres', y="Medias", color='Pessoas', barmode='group',
                        range_color='red')
    return imagem


if __name__ == '__main__':
    # webbrowser.open_new_tab('http://127.0.0.1:8050/')
    app.run_server(debug=True)
