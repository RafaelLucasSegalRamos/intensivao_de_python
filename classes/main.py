class ControleRemoto:
    def __init__(self, cor, largura, altura, profundidade):
        self.profundidade = profundidade
        self.cor = cor
        self.largura = largura
        self.altura = altura

    def passar_canal(self, botao):
        b = str(botao)
        if b == '+':
            print('Passar o canal 1 a frente')
        elif b == '-':
            print('Voltar em 1 o canal')


# nas classes sempre terá a função __init__():
controle_remoto = ControleRemoto(cor='preto', largura='10cm', altura='2cm', profundidade='3cm')
controle_remoto2 = ControleRemoto(cor='cinza', largura='7.5cm', altura='2cm', profundidade='2cm')
print(controle_remoto.profundidade)
print(controle_remoto2.cor)
controle_remoto.passar_canal(botao="+")

