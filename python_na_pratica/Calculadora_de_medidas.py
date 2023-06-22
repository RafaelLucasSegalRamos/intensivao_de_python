from tkinter import *
from tkinter import ttk
import os

janela = Tk()
janela.title("Calculadora de medidas")
janela.geometry("1000x400")
janela.resizable(False, False)
janela.iconbitmap(os.path.join('imgs/favicon.ico'))


def med_escolhido():
    pass


Med_escohido = StringVar()
Med_escohido.set("Escolha uma opção")

cor_fundo = "#444"
azul_claro = "#87FAFA"

# Frames
frame_title = Frame(janela, width=700, height=100, borderwidth=2, relief='solid', bg=cor_fundo, padx=10, pady=10)
frame_title.grid(row=0, column=0)
frame_options = Frame(janela, width=700, height=300, borderwidth=2, relief='solid', bg=cor_fundo, padx=10, pady=10)
frame_options.grid(row=1, column=0)
frame_escolhido = Frame(janela, width=300, height=100, borderwidth=2, relief='solid', bg=cor_fundo, padx=10, pady=10)
frame_escolhido.grid(row=0, column=1)
frame_converte = Frame(janela, width=300, height=300, borderwidth=2, relief='solid', bg=cor_fundo, padx=10, pady=10)
frame_converte.grid(row=1, column=1)

# Botões
btn_massa = Button(frame_options, text="Massa", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=17, height=2,
                   borderwidth=0)
btn_massa.place(x=10, y=10)

btn_tempo = Button(frame_options, text="Tempo", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=17, height=2,
                   borderwidth=0)
btn_tempo.place(x=235, y=10)

btn_comprimento = Button(frame_options, text="Comprimento", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=17,
                         height=2, borderwidth=0)
btn_comprimento.place(x=460, y=10)

btn_area = Button(frame_options, text="Área", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=17, height=2,
                  borderwidth=0)
btn_area.place(x=10, y=100)

btn_volume = Button(frame_options, text="Volume", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=17, height=2,
                    borderwidth=0)
btn_volume.place(x=235, y=100)

btn_velocidade = Button(frame_options, text="Velocidade", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=17,
                        height=2, borderwidth=0)
btn_velocidade.place(x=460, y=100)

btn_temperatura = Button(frame_options, text="Temperatura", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=17,
                         height=2, borderwidth=0)
btn_temperatura.place(x=10, y=190)

btn_energia = Button(frame_options, text="Energia", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=17,
                     height=2, borderwidth=0)
btn_energia.place(x=235, y=190)

btn_pressao = Button(frame_options, text="Pressão", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=17,
                     height=2, borderwidth=0)
btn_pressao.place(x=460, y=190)

# Labels
label_title = Label(frame_title, text="Calculadora de unidades de medidas", font="Arial 20 bold", bg=cor_fundo,
                    fg=azul_claro)
label_title.place(x=80, y=20)

label_escolhido = Label(frame_escolhido, font="Arial 20 bold", bg=cor_fundo, fg=azul_claro,
                        textvariable=Med_escohido)
label_escolhido.place(x=10, y=25)
janela.mainloop()

# Icone pegos no https://icons8.com/icon/qQjEczFlZAB2/peso
