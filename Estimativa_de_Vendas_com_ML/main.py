import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3


def EncontraY(x_reta, y_reta, x):
    a = (y_reta[1] - y_reta[0]) / (x_reta[1] - x_reta[0])
    b = y_reta[0] - a * x_reta[0]
    y = a * x + b
    return y


base = pd.read_excel('Investimento_x_Venda.xlsx')

plt.scatter(base['Investimento em marketing'], base['Venda Qtd'])

x0 = base['Investimento em marketing'][0]
x1 = base['Investimento em marketing'][6]
y0 = base['Venda Qtd'][0]
y1 = base['Venda Qtd'][6]
plt.scatter(75, EncontraY([x0, x1], [y0, y1], 75), color='k')
plt.plot([x0, x1], [y0, y1], 'r')
plt.show()
