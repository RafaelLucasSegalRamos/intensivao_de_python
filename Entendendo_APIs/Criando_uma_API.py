import flask as fk
import json
import pandas as pd

app = fk.Flask(__name__)


@app.route("/")
def homepage():
    return "<h1 style='font-family: Arial;''>Está é a HomePage da API<h1>"


@app.route("/pegarvendas")
def pegarvendas():
    tabela = pd.read_csv('tebelinha.csv')
    tot_vendas = tabela["Vendas"].sum()
    resposta = {"total de vendas": f"{tot_vendas:.2f}", "Maior venda": f"{tabela['Vendas'].max():.2f}",
                "Menor venda": f"{tabela['Vendas'].min():.2f}"}
    return fk.jsonify(resposta)


app.run(host="0.0.0.0", port=8080)  # No caso o host e o port é apena para a versão online que fiz
