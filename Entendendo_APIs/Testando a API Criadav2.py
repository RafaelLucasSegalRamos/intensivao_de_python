import requests
import json
import os

# arquivo = open('infor_de_Vendas.txt', 'w')
link = "http://localhost:5000/livros"  # Por este ser um link local talvez va funcionar no seu tambem caso você tenha uma API neste link
response = requests.get(link)
# print(response.status_code)
infor = response.json()

print(response)
for i in infor:
    for j, k in sorted(i.items()):
        print(f"{j}: {k}", end=' ')
    print()

    # arquivo.write(f"{k}: {i}\n")

# arquivo.close()

# os.startfile('infor_de_Vendas.txt')