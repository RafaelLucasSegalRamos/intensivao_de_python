import pandas as pd
import openpyxl
from twilio.rest import Client

# Passo de solução

# Abrir os 6 arquivos em Excel
mounth_list = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
sell_table = list()

for mounth in mounth_list:
    sell_table = pd.read_excel(f'{mounth}.xlsx')
    if (sell_table['Vendas'] >= 55000).any():
        worker = sell_table.loc[sell_table['Vendas'] >= 55000, 'Vendedor'].values[0]
        sold = sell_table.loc[sell_table['Vendas'] >= 55000, 'Vendas'].values[0]
        print(f'No mês de {mounth} o funcionário {worker} vendeu R${sold},00')


acount_sid = "AC97acb3271ecdd28d1c89b2d50d1a7cad"
auth_token = '0a362c979f9a6606cdfdc76d9a62dc73'

client = Client(acount_sid, auth_token)

message = client.messages.create(
    to="+5519996534693",
    from_="+19035231705",
    body=f"Eai Will :)"
)


# Para cada arquivo:
# Verificar se algum valor no arquivo é maior que 55.000 na coluna vendas.
# Se maior que 55.000 manda pro SMS no nosso número com o nome e vendas do funcionário
# Caso não tenha valor acima de 55.000 nada acontecerá.
