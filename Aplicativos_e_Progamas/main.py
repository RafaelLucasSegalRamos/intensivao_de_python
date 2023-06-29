# importar o app, builder (GUI)
from kivy.app import App
from kivy.lang import Builder

# Indicando a tela do app
GUI = Builder.load_file("tela.kv")  # carregar o arquivo tela.kv


# criar o app

class AppPrincipal(App):
    def build(self):
        return GUI

# criar a função build

AppPrincipal().run()