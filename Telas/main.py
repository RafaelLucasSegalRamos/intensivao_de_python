import requests as rq
from tkinter import *


def troll():
    trola = Label(master=janela, text='Comi o cu de quem ta lendo')
    trola.grid(column=3, row=9)


janela = Tk()
janela.title('Teste de janelas em python')
texto = Label(master=janela, text='Clique no botão para ver uma coisa!')
texto.grid(column=3, row=3)
botao = Button(master=janela, text='Clique Aqui!!', command=troll)
botao.grid(column=3, row=6)
janela.mainloop()
