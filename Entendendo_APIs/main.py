# Exemplo de API de cotação de moedas

import requests
import json


def get_cotacao():
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


if __name__ == '__main__':
    for t in get_cotacao():
        print("-=-" * 10)
        for k, v in get_cotacao()[t].items():
            if k == "bid" or k == "code" or k == "codein" or k == "name":
                print(f"{k}: {v}")
        print("-=-" * 10)
