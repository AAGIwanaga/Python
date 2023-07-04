class Pessoa:
    def acao(self):
        print(f'Inicializando o sistema')

class Acao1(Pessoa):
    def acao(self):
        print('Sistema pronto para uso')

class Acao2(Pessoa):
    def acao(self):
        print('Desligando o sistema')

class SaveJogador1(Acao1, Acao2):
    pass

p1 = SaveJogador1()
p1.acao()