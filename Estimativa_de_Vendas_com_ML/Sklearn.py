import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_excel('Investimento_x_Venda.xlsx')
inves = float(input('Digite o valor do investimento em marketing: '))
reg = LinearRegression().fit(base['Investimento em marketing'].values.reshape(-1, 1),
                             base['Venda Qtd'].values.reshape(-1, 1))
# Neste Linear Regresion para podermos utilizar os valores na coluna de investimento em marketing e venda qtd temos
# que utilizar o reshape(-1, 1) para que o algoritmo entenda que estamos trabalhando com os valores em si e não com
# os valores do tipo Series. O -1 significa que não importa quantas linhas tenha, e o 1 significa que queremos apenas
print(reg.coef_)  # coeficiente angular
print(reg.intercept_)  # coeficiente linear

plt.scatter(base['Investimento em marketing'], base['Venda Qtd'])
plt.scatter(inves, reg.predict([[inves]]), color='violet')
x = np.array(base['Investimento em marketing'])
reg.predict([[inves]])

y = reg.coef_[0][0] * x + reg.intercept_[0]
plt.plot(x, y, color='r')
plt.show()
