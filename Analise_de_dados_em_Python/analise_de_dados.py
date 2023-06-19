import pandas as pd

tabela = pd.read_excel('Vendas.xlsx')

faturamento_total = float(tabela["Valor Final"].sum())
print(f'Faturamento total de todas as lojas: \033[92mR${str(faturamento_total).replace(".", ",")}\033[m')

faturamento_por_loja = tabela[['ID Loja', 'Valor Final']].groupby("ID Loja").sum()
print(faturamento_por_loja)

faturamento_por_produto = tabela[['ID Loja', 'Produto', 'Valor Final']].groupby(["ID Loja", "Produto"]).sum()
print(faturamento_por_produto)
