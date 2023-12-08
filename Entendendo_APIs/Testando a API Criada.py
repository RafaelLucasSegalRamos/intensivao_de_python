import requests
import json
import os

arquivo = open('infor_de_Vendas.txt', 'w')
link = "https://python-api--rafaelramos811.repl.co/pegarvendas"  # Link da API que criei, mas que provavelmente se você tentar utiliza-la,
# não vai funcionar, pois ela está hospedada no repl.it, e provavelmete eu já terei parado a aplicação
response = requests.get(link)
# print(response.status_code)
infor = response.json()

for k, i in infor.items():
    arquivo.write(f"{k}: {i}\n")

arquivo.close()

os.startfile('infor_de_Vendas.txt')