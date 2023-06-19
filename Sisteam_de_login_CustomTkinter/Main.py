"""import tkinter

janela = tkinter.Tk()
janela.geometry("700x500")


def click():
    print("Você clicou!")


text = tkinter.Label(janela, text='Olá bem vindo!')
text1 = tkinter.Label(text='Para entrar no aplicativo conclua o login abaixo!')

text.pack(padx=10, pady=20)
text1.pack()

botao = tkinter.Button(janela, text='Concluir o login!', command=click)
botao.pack(padx=20, pady=30)

janela.mainloop()"""

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')
janela = customtkinter.CTk()
janela.geometry("700x500")


def click():
    print("Você clicou!")


text = customtkinter.CTkLabel(janela, text='Olá Bem vindo!', text_color='white')
text1 = customtkinter.CTkLabel(janela, text='Para entrar no aplicativo conclua o login abaixo!', text_color='white')
text.pack(padx=10, pady=20)
text1.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text='Coloque seu email', placeholder_text_color='lightblue',
                               border_width=0, fg_color=('#222', '#111'), text_color='#00cccc', corner_radius=5)
email.pack(padx=10, pady=10)
senha = customtkinter.CTkEntry(janela, placeholder_text='Coloque sua senha', placeholder_text_color='lightblue',
                               border_width=0, fg_color=('#222', '#111'), text_color='#00cccc', corner_radius=5,
                               show='*')
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text='Lembrar de email e senha?')
checkbox.pack()

botao = customtkinter.CTkButton(janela, text="Concluir o Login", command=click, text_color="white", fg_color='#333',
                                hover_color='#444', corner_radius=10)
botao.pack(padx=10, pady=30)

janela.mainloop()
