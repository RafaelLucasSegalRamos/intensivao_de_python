# Essa API é par explicar o uso de API com Paginação

import json
import openpyxl
import pandas as pd
import requests as rs

tf = pd.DataFrame()
pula_vlr = 0

while True:
# link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=1000&$orderby=Data%20desc&$format=json&$select=Data,Quantidade,Valor,Denominacao,Especie"
    link = f"https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=1000&$skip={pula_vlr}&$orderby=Data%20desc&$format=json&$select=Data,Quantidade,Valor,Denominacao,Especie"

    response = rs.get(link)
    infor = response.json()

    tabela = pd.DataFrame(infor["value"])
    if len(infor["value"]) < 1:
        break
    tf = pd.concat([tf, tabela])
    pula_vlr += 1000

    # tabela = pd.DataFrame(infor["value"])
    # tabela["Data"] = pd.to_datetime(tabela["Data"])
    # tabela["Valor"] = tabela["Valor"].map("{:,.2f}".format)
    # tabela["Quantidade"] = tabela["Quantidade"].map("{:,}".format)

print(tabela)