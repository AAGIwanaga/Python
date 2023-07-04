class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def Acao1(self):
        print(f'{self.nome} está dormindo')

class Jogador1(Pessoa):
    def Acao2(self):
        print(f'{self.nome} está comendo')

class SaveJogador1(Jogador1):
    def Acao1(self):
        print(f'{self.nome} está acordado') #SOBREPOSIÇÃO DA 'Acao1' DE '... dormindo' PARA '...acordado'

p1 = SaveJogador1('André')
print(p1.nome)
p1.Acao1()
p1.Acao2()