from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk, Image

janela = Tk()
janela.title("Calculadora de medidas")
janela.geometry("1000x400")
janela.resizable(False, False)
janela.iconbitmap(os.path.join('imgs/favicon.ico'))

# Funções

unidades_valores = []
unidade_para = []
unidade_de = []
unidades = {'Massa': [{'Kg': 1000}, {'Hg': 100}, {'Dag': 10}, {'G': 1}, {'Dg': 0.1}, {'Cg': 0.01}, {'Mg': 0.001},
                      {'Lb': 453.592}, {'Oz': 28.3495}, {'St': 6350.29}],
            'Tempo': [{'Seg': 1}, {'Min': 60}, {'Hora': 3600}, {'Dia': 86400}, {'Semana': 604800}, {'Mês': 2628000}, {'Ano': 31536000}],
            'Comprimento': [{'km': 1000}, {'hm': 100}, {'dam': 10}, {'m': 1}, {'dm': 0.1}, {'cm': 0.01}, {'mm': 0.001},
                            {'mi': 1609.34}, {'yd': 0.9144}, {'ft': 0.3048}, {'in': 0.0254}],
            'Área': [{'km²': 1000000}, {'hm²': 10000}, {'dam²': 100}, {'m²': 1}, {'dm²': 0.01}, {'cm²': 0.0001},
                     {'mm²': 0.000001}, {'mi²': 2589988.11}, {'yd²': 0.836127}, {'ft²': 0.092903}, {'in²': 0.00064516},
                     {'ac': 4046.86}, {'a': 100}, {'ha': 10000}],
            'Volume': [{'km³': 1000000000}, {'hm³': 1000000}, {'dam³': 1000}, {'m³': 1}, {'dm³': 0.001},
                       {'cm³': 0.000001}, {'mm³': 0.000000001}, {'mi³': 4168181825.44}, {'yd³': 0.764555},
                       {'ft³': 0.0283168}, {'in³': 0.0000163871}, {'ac-ft': 1233.48}, {'gal': 0.00378541},
                       {'qt': 0.000946353}, {'pt': 0.000473176}, {'fl oz': 0.0000295735}, {'bbl': 0.158987},
                       {'l': 0.001}, {'dl': 0.0001}, {'cl': 0.00001}, {'ml': 0.000001}],
            'Velocidade': [{'km/h': 1}, {'m/s': 3.6}, {'mi/h': 1.60934}, {'ft/s': 1.09728}, {'kn': 1.852}],
            'Temperatura': [{'°C': 1}, {'°F': 1.8}, {'K': 1}],
            'Pressão': [{'Pa': 1}, {'kPa': 1000}, {'MPa': 1000000}, {'bar': 100000}, {'mbar': 100}, {'psi': 6894.76},
                        {'ksi': 6894757.29}, {'mmHg': 133.322}, {'atm': 101325}, {'at': 98066.5}, {'torr': 133.322}],
            'Energia': [{'J': 1}, {'kJ': 1000}, {'MJ': 1000000}, {'cal': 4.184}, {'kcal': 4184}, {'Wh': 3600},
                        {'kWh': 3600000}, {'MWh': 3600000000}, {'BTU': 1055.06}, {'ft-lb': 1.35582},
                        {'in-lb': 0.112985}, {'hp-h': 2684519.54}]
            }


def mostra_menu(event):

    unidades_valores = []
    unidade_para = []
    unidade_de = []
    for j in unidades[event]:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidades_valores.append(v)

    cb_de['values'] = unidade_de
    cb_para['values'] = unidade_para
    Med_escohido.set(event)

def calcula():
    global unidades

    valor = float(valorentry.get())
    for j in unidades:
        if Med_escohido.get() == j:
            print(j)
            for k in unidades[j]:
                print(k)
                for l, v in k.items():
                    if cb_de.get() == l:
                        print(l, v)
                        de = v
                    if cb_para.get() == l:
                        print(l, v)
                        para = v
            valorsaida.set(valor * (de / para))








# Variáveis

Med_escohido = StringVar()
Med_escohido.set("Escolha uma opção")
valorde = StringVar()
valorpara = StringVar()
valorentry = StringVar()
valorentry.set("1")
valorsaida = StringVar()

cor_fundo = "#444"
azul_claro = "#87FAFA"

# Frames
frame_title = Frame(janela, width=700, height=100, borderwidth=2, relief='solid', bg=cor_fundo, padx=10, pady=10)
frame_title.place(x=0, y=0)
frame_options = Frame(janela, width=700, height=300, borderwidth=2, relief='solid', bg=cor_fundo, padx=10, pady=10)
frame_options.place(x=0, y=100)
frame_escolhido = Frame(janela, width=300, height=100, borderwidth=2, relief='solid', bg=cor_fundo, padx=10, pady=10)
frame_escolhido.place(x=700, y=0)
frame_converte = Frame(janela, width=300, height=300, borderwidth=2, relief='solid', bg=cor_fundo, padx=10, pady=10)
frame_converte.place(x=700, y=100)

# Botões
img_massa = Image.open("imgs/peso.png")
img_massa = img_massa.resize((50, 50), Image.LANCZOS)
img_massa = ImageTk.PhotoImage(img_massa)

btn_massa = Button(frame_options, text="Peso", image=img_massa, font="Arial 15 bold", bg=azul_claro, fg=cor_fundo,
                   width=210, height=60,
                   borderwidth=0, anchor=CENTER, compound=LEFT, command=lambda: mostra_menu("Massa"))
btn_massa.place(x=10, y=10)

img_tempo = Image.open("imgs/clock.png")
img_tempo = img_tempo.resize((50, 50), Image.LANCZOS)
img_tempo = ImageTk.PhotoImage(img_tempo)

btn_tempo = Button(frame_options, text="Tempo", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=210, height=60,
                   borderwidth=0, image=img_tempo, compound=LEFT, anchor=CENTER, command=(lambda: mostra_menu("Tempo")))
btn_tempo.place(x=235, y=10)

img_comprimento = Image.open("imgs/Ruler.png")
img_comprimento = img_comprimento.resize((50, 50), Image.LANCZOS)
img_comprimento = ImageTk.PhotoImage(img_comprimento)

btn_comprimento = Button(frame_options, text="Comprimento", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo,
                         width=210, height=60, borderwidth=0, image=img_comprimento, compound=LEFT, anchor=CENTER, command=(lambda: mostra_menu("Comprimento")))
btn_comprimento.place(x=460, y=10)

img_area = Image.open("imgs/square.png")
img_area = img_area.resize((50, 50), Image.LANCZOS)
img_area = ImageTk.PhotoImage(img_area)

btn_area = Button(frame_options, text="Área", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=210, height=60,
                  borderwidth=0, image=img_area, compound=LEFT, anchor=CENTER, command=(lambda: mostra_menu("Área")))
btn_area.place(x=10, y=100)

img_volume = Image.open("imgs/volume.png")
img_volume = img_volume.resize((50, 50), Image.LANCZOS)
img_volume = ImageTk.PhotoImage(img_volume)

btn_volume = Button(frame_options, text="Volume", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=210,
                    height=60,
                    borderwidth=0, image=img_volume, compound=LEFT, anchor=CENTER, command=(lambda: mostra_menu("Volume")))
btn_volume.place(x=235, y=100)

img_velocidade = Image.open("imgs/speedometer.png")
img_velocidade = img_velocidade.resize((50, 50), Image.LANCZOS)
img_velocidade = ImageTk.PhotoImage(img_velocidade)

btn_velocidade = Button(frame_options, text="Velocidade", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=210,
                        height=60, borderwidth=0, image=img_velocidade, compound=LEFT, anchor=CENTER, command=(lambda: mostra_menu("Velocidade")))
btn_velocidade.place(x=460, y=100)

img_temperatura = Image.open("imgs/termometro.png")
img_temperatura = img_temperatura.resize((50, 50), Image.LANCZOS)
img_temperatura = ImageTk.PhotoImage(img_temperatura)

btn_temperatura = Button(frame_options, text="Temperatura", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo,
                         width=210, height=60, borderwidth=0, image=img_temperatura, compound=LEFT, anchor=CENTER, command=(lambda: mostra_menu("Temperatura")))
btn_temperatura.place(x=10, y=190)

img_energy = Image.open("imgs/bateria.png")
img_energy = img_energy.resize((50, 50), Image.LANCZOS)
img_energy = ImageTk.PhotoImage(img_energy)

btn_energia = Button(frame_options, text="Energia", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=210,
                     height=60, borderwidth=0, image=img_energy, compound=LEFT, anchor=CENTER, command=(lambda: mostra_menu("Energia")))
btn_energia.place(x=235, y=190)

btn_calcula = Button(frame_converte, text="Calcular", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=8,
                     height=1, borderwidth=0, anchor=CENTER, command=calcula)
btn_calcula.place(x=170, y=120)

img_pressure = Image.open("imgs/pressure.png")
img_pressure = img_pressure.resize((50, 50), Image.LANCZOS)
img_pressure = ImageTk.PhotoImage(img_pressure)

btn_pressao = Button(frame_options, text="Pressão", font="Arial 15 bold", bg=azul_claro, fg=cor_fundo, width=210,
                     height=60, borderwidth=0, image=img_pressure, compound=LEFT, anchor=CENTER, command=(lambda: mostra_menu("Pressão")))
btn_pressao.place(x=460, y=190)

# Labels
label_title = Label(frame_title, text="Calculadora de unidades de medidas", font="Arial 20 bold", bg=cor_fundo,
                    fg=azul_claro)
label_title.place(x=80, y=20)

label_escolhido = Label(frame_escolhido, font="Arial 20 bold", bg=cor_fundo, fg=azul_claro,
                        textvariable=Med_escohido)
label_escolhido.place(x=10, y=20)

la_digi = Label(master=frame_converte, font="Arial 16 bold", bg=cor_fundo, fg=azul_claro,
                text="Digite o número abaixo:")
la_digi.place(x=0, y=60)

l_de = Label(master=frame_converte, font="Arial 16 bold", bg=cor_fundo, fg=azul_claro, text="De:")
l_de.place(x=0, y=10)

l_para = Label(master=frame_converte, font="Arial 16 bold", bg=cor_fundo, fg=azul_claro, text="Para:")
l_para.place(x=135, y=10)

cb_de = ttk.Combobox(master=frame_converte, font="Arial 16 bold", width=5, textvariable=valorde, justify=CENTER)
cb_de.place(x=45, y=10)

cb_para = ttk.Combobox(master=frame_converte, font="Arial 16 bold", width=5, textvariable=valorpara, justify=CENTER)
cb_para.place(x=200, y=10)

# Entry

e_entrada = Entry(master=frame_converte, font="Arial 20 bold", width=10, textvariable=valorentry, justify=CENTER)
e_entrada.place(x=0, y=120)

e_saida = Entry(master=frame_converte, font="Arial 20 bold", width=10, textvariable=valorsaida, justify=CENTER)
e_saida.place(x=0, y=180)

# Icone pegos no https://icons8.com/icon/qQjEczFlZAB2/peso

janela.mainloop()
