class Carros:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def descricao(self):
        print(f'O carro {self.nome} é {self.cor}')

class Gol(Carros):
    def __init__(self, nome, cor):
        super().__init__(nome, cor) #super() É A FUNÇÃO RESPONSÁVEL POR HERDAR AS INFORMAÇÕES CONTIDAS NA CLASSE MÃE
    
class Corsa(Carros):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

gol1 = Gol('Gol 2019 Completo', 'Branco')
corsa2 = Corsa('Corsa 2017 2 Portas', 'vermelho') 

print(gol1.descricao())
print(corsa2.descricao())