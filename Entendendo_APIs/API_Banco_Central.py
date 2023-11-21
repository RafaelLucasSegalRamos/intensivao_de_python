# Essa API é par explicar o uso de API com Paginação

import json
import openpyxl
import pandas as pd
import requests as rs

tf = pd.DataFrame()
pula_vlr = 0

try:
    while True:
        # link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=1000&$orderby=Data%20desc&$format=json&$select=Data,Quantidade,Valor,Denominacao,Especie"
        link = f"https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=1000&$skip={pula_vlr}&$orderby=Data%20desc&$format=json&$select=Data,Quantidade,Valor,Denominacao,Especie"

        response = rs.get(link)
        infor = response.json()

        tabela = pd.DataFrame(infor["value"])
        tf = pd.concat([tf, tabela])
        pula_vlr += 10000

        if not bool(tabela["value"]):
            break


except:
    print("Fim da paginação")
finally:
    tf = pd.DataFrame(infor["value"])
    tf["Data"] = pd.to_datetime(tf["Data"])
    tf["Valor"] = tf["Valor"].map("{:,.2f}".format)
    tf["Quantidade"] = tf["Quantidade"].map("{:,}".format)
    print(tf)
