class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.list_planos = ['Master Premium', 'Premium', 'Basic']
        if plano in self.list_planos:
            self.plano = plano
        else:
            print('Este não é um dos planos possiveis')

    def add_to_data_base(self):
        pass


cliente = Cliente(nome='Rafael', email='teste@gmail.com', plano='Master Premium')
cliente.add_to_data_base()
