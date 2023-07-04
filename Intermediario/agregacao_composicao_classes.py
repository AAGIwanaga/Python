class Contato: #CRIAÇÃO DA CLASSE 'Contato'
    def __init__(self, residencial, celular): #DEFINE OS OBJETOS DE 'residencial' E 'celular'
        self.residencial = residencial
        self.celular = celular

class Cliente: #CRIAÇÃO DA CLASSE 'Cliente'
    def __init__(self, nome, idade, fone = None): #DEFINIÇÃO DOS OBJETOS 'nome', 'idade', E 'fone= LISTA VAZIA'
        self.nome = nome
        self.idade = idade
        self.fone = [] #COLCHETES SIGNIFICA QUE É LISTA

    def addFone(self, residencial, celular): # DEFINIÇÃO DA FUNÇÃO 'addFone', COM OS PARAMETROS 'residencial' E 'celular' OS QUAIS FORAM INSTALCIADOS EM OUTRA CLASSE 'Contato'
        self.fone.append(Contato(residencial,celular)) # CASO HAJA QUALQUER EXCEÇÃO NO CÓDIGO, TUDO IRÁ PARAR DE FUNCNIONAR

    def listaFone(self):
        for fone in self.fone:
            print(fone.residencial, fone.celular)

cliente1 = Cliente('Fernando', 32)
cliente1.addFone(33221766, 991357258)
print(cliente1.nome)
print(cliente1.listaFone())