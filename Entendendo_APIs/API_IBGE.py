import requests
import json


link = "https://servicodados.ibge.gov.br/api/v3/agregados/8418/periodos/2019/variaveis/12749|12750|12752|12753?localidades=N2[all]"

response = requests.get(link)
# print(response.status_code)
for i in response.json():
    for j in i:
        print(j)
        print(i[j])
        print("-=-" * 10)
