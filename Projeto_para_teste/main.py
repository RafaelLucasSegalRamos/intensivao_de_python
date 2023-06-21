class Pessoa:
    def __init__(self, nome, idade, anoNas):
        self.idade = idade
        self.nome = nome
        self.anoNas = anoNas
        self.telefone = list()

    def addTel(self, telefone):
        self.telefone.append(telefone)

    def __str__(self):
        return f'Meu nome é {self.nome}, tenho {self.idade} anos, pois nasci em {self.anoNas}, e meus meio de contaos,' \
               f' pelo menos por telefone é {self.telefone}'


class Telefone:
    def __init__(self, id, numero, operadora):
        self.id = id
        self.numero = numero
        self.operadora = operadora

    def __str__(self):
        return f"""Id do Telefone:{self.id}, Numero do Telefone:{self.numero}, Operadora:{self.operadora}"""


rafael = Pessoa('Rafael', '18', '2005')
T1 = Telefone(1, '19996534693', 'Vivo')
T2 = Telefone(2, '19996548215', 'Vivo')
rafael.addTel(T2.numero)
rafael.addTel(T1.numero)
print(rafael)
print(T1)


class Cliente(Pessoa):
    def __init__(self, registro, nome, idade, anoNas):
        super.__init__(nome, idade, anoNas)
        self.registro = registro


c1 = Cliente(rafael)
c1.registro = 3

c1.addTel('12332442355')
