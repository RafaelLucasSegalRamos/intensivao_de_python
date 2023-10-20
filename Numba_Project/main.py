import time
from numba import jit, njit

try:
    @jit(nopython=True) # Ou podemos usar o njit
    def valor_com_imposto(qtde):
        for i in range(qtde):
            if i == 0:
                novo_valor = qtde * 1.1
            else:
                novo_valor *= 1.1
        return novo_valor


    inicio = time.time()
    teste = valor_com_imposto(10000000)

    print(teste)
except Exception as erro:
    print(erro.__class__)

finally:
    fim = time.time()
    print(f"Tempo do progama: {(fim - inicio):.2f}")
