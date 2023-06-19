from tkinter import *
from playsound import playsound
from gtts import *
import os

janela = Tk()

janela.title('Gerador de falas a partir de texto')
janela.geometry('800x600')
janela.maxsize(800, 600)
janela.minsize(400, 300)
janela.configure(bg='#1d1d1d')

titulo = Label(janela, text='Bem vindo ao progama!', bg='#1d1d1d', fg='white', font=('Arial', 20, 'bold'))

titulo.pack()

janela.mainloop()
