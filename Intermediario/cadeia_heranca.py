class Carro:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

class Gasolina(Carro):
    def __init__(self, tipogasolina = True, tipoalcool = False):
        self.tipogasolina = tipogasolina
        self.tipoalcool = tipoalcool

class Jeep(Gasolina): # CÓDIGO EFICIENTE, SEGUINDO UMA HIERARQUIA, A QUAL A CLASSE 'Carro' PODERÁ SER REAPROVEITADA EM OUTROS TIPOS DE CARROS
    pass

carro1 = Jeep()
print(carro1.tipogasolina)







'''EFICIENTE VS INEFICIENTE'''

class Jeep:
    def carro():
        def __init__(self, nome, ano):
            self.nome = nome
            self.ano = ano

    def gasolina(self, tipogasolina = True, tipoalcool = False):
        self.tipogasolina = tipogasolina
        self.tipoalcool = tipoalcool

jeep = Jeep() # NÃO SERIA POSSIVEL REAPROVEITAR NADA DESTA CLASSE 'Jeep' PARA OUTROS CARROS