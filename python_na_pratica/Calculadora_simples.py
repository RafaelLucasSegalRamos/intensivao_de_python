from tkinter import *
from tkinter import ttk


def command_c():
    inittext.set('0')
    global todos_valores
    todos_valores = ''


todos_valores = ''


def pega_valor(evento):
    global todos_valores
    todos_valores += str(evento)
    inittext.set(todos_valores)
    # inittext.set(str(result).replace('.', ','))


def calcula():
    try:
        global todos_valores
        todos_valores = todos_valores.replace('x', '*')
        todos_valores = todos_valores.replace('÷', '/')
        if '**' in todos_valores:
            inittext.set('Equação Inválida.')
        if '*-+' in todos_valores:
            inittext.set('Equação Inválida.')
        if '*+-' in todos_valores:
            inittext.set('Equação Inválida.')
        else:
            resultado = eval(todos_valores)
            todos_valores = str(resultado)
            inittext.set(todos_valores)
    except SyntaxError:
        inittext.set('Equação Inválida.')
    except ZeroDivisionError:
        inittext.set('Impos. dividir por 0.')


janela = Tk()
cor1 = '#333'
cor2 = '#ddd'
cor3 = '#62b'
cor4 = '#aaa'
cor5 = '#FFAb40'
janela.title('Calculadora feita em python')
janela.geometry('235x300')
janela.configure(background=cor1)
janela.iconbitmap('favicon.ico')

frame_head = Frame(janela, width=235, height=50, bg='#444')
frame_head.grid(row=0, column=0)

frame_corp = Frame(janela, width=235, height=268)
frame_corp.grid(row=1, column=0)

btnC = Button(frame_corp, text='C', width=11, height=2, bg=cor4, borderwidth=0, fg=cor2, relief=RAISED,
              overrelief=RIDGE, font='Arial 13 bold', command=command_c)
btnC.place(x=0, y=0)

btnPor = Button(frame_corp, text='%', width=5, height=2, bg=cor4, borderwidth=0, fg=cor2, relief=RAISED,
                overrelief=RIDGE, font='Arial 13 bold', command=lambda: pega_valor('%'))
btnPor.place(x=120, y=0)

btnDiv = Button(frame_corp, text='/', width=5, height=2, bg=cor3, borderwidth=0, fg=cor2, relief=RAISED,
                overrelief=RIDGE, font='Arial 13 bold', command=lambda: pega_valor('/'))
btnDiv.place(x=180, y=0)

btn7 = Button(frame_corp, text='7', width=5, height=2, bg=cor2, borderwidth=0, fg=cor1, relief=RAISED, overrelief=RIDGE,
              font='Arial 13 bold', command=lambda: pega_valor('7'))
btn7.place(x=0, y=50)

btn8 = Button(frame_corp, text='8', width=5, height=2, bg=cor2, borderwidth=0, fg=cor1, relief=RAISED, overrelief=RIDGE,
              font='Arial 13 bold', command=lambda: pega_valor('8'))
btn8.place(x=60, y=50)

btn9 = Button(frame_corp, text='9', width=5, height=2, bg=cor2, borderwidth=0, fg=cor1, relief=RAISED, overrelief=RIDGE,
              font='Arial 13 bold', command=lambda: pega_valor('9'))
btn9.place(x=120, y=50)

btnMult = Button(frame_corp, text='*', width=5, height=2, bg=cor3, borderwidth=0, fg=cor2, relief=RAISED,
                 overrelief=RIDGE, font='Arial 13 bold', command=lambda: pega_valor('*'))
btnMult.place(x=180, y=50)

btn4 = Button(frame_corp, text='4', width=5, height=2, bg=cor2, borderwidth=0, fg=cor1, relief=RAISED, overrelief=RIDGE,
              font='Arial 13 bold', command=lambda: pega_valor('4'))
btn4.place(x=0, y=100)

btn5 = Button(frame_corp, text='5', width=5, height=2, bg=cor2, borderwidth=0, fg=cor1, relief=RAISED, overrelief=RIDGE,
              font='Arial 13 bold', command=lambda: pega_valor('5'))
btn5.place(x=60, y=100)

btn6 = Button(frame_corp, text='6', width=5, height=2, bg=cor2, borderwidth=0, fg=cor1, relief=RAISED, overrelief=RIDGE,
              font='Arial 13 bold', command=lambda: pega_valor('6'))
btn6.place(x=120, y=100)

btnSub = Button(frame_corp, text='-', width=5, height=2, bg=cor3, borderwidth=0, fg=cor2, relief=RAISED,
                overrelief=RIDGE, font='Arial 13 bold', command=lambda: pega_valor('-'))
btnSub.place(x=180, y=100)

btn1 = Button(frame_corp, text='1', width=5, height=2, bg=cor2, borderwidth=0, fg=cor1, relief=RAISED, overrelief=RIDGE,
              font='Arial 13 bold', command=lambda: pega_valor('1'))
btn1.place(x=0, y=150)

btn2 = Button(frame_corp, text='2', width=5, height=2, bg=cor2, borderwidth=0, fg=cor1, relief=RAISED, overrelief=RIDGE,
              font='Arial 13 bold', command=lambda: pega_valor('2'))
btn2.place(x=60, y=150)

btn3 = Button(frame_corp, text='3', width=5, height=2, bg=cor2, borderwidth=0, fg=cor1, relief=RAISED, overrelief=RIDGE,
              font='Arial 13 bold', command=lambda: pega_valor('3'))
btn3.place(x=120, y=150)

btnSoma = Button(frame_corp, text='+', width=5, height=2, bg=cor3, borderwidth=0, fg=cor2, relief=RAISED,
                 overrelief=RIDGE, font='Arial 13 bold', command=lambda: pega_valor('+'))
btnSoma.place(x=180, y=150)

btn0 = Button(frame_corp, text='0', width=11, height=2, bg=cor2, borderwidth=0, fg=cor1, relief=RAISED,
              overrelief=RIDGE, font='Arial 13 bold', command=lambda: pega_valor('0'))
btn0.place(x=0, y=200)

btnPonto = Button(frame_corp, text='.', width=5, height=2, bg=cor4, borderwidth=0, fg=cor2, relief=RAISED,
                  overrelief=RIDGE, font='Arial 13 bold', command=lambda: pega_valor('.'))
btnPonto.place(x=120, y=200)

btnIgual = Button(frame_corp, text='=', width=5, height=2, bg=cor3, borderwidth=0, fg=cor2, relief=RAISED,
                  overrelief=RIDGE, font='Arial 13 bold', command=calcula)
btnIgual.place(x=180, y=200)

# Labels
inittext = StringVar()

app_label = Label(frame_head, font='Arial 13 bold', padx=7, width=16, height=2, relief=FLAT, bg='#444',
                  fg=cor2, anchor='e', textvariable=inittext, justify=RIGHT)
app_label.place(x=0, y=3)

janela.mainloop()
