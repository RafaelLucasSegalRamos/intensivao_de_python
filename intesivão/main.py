import pandas as pd
import openpyxl
from twilio.rest import Client
import Secrets

codes = Secrets()
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


acount_sid = codes.ACCAUNT_SID
auth_token = codes.AUTH_TOKEN

client = Client(acount_sid, auth_token)

message = client.messages.create(
    to=codes.MY_PHONE_NUMBER,
    from_=codes.PHONE_NUMBER,
    body=f"Eai {codes.RANDOM_NAME} :)"
)


# Para cada arquivo:
# Verificar se algum valor no arquivo é maior que 55.000 na coluna vendas.
# Se maior que 55.000 manda pro SMS no nosso número com o nome e vendas do funcionário
# Caso não tenha valor acima de 55.000 nada acontecerá.
