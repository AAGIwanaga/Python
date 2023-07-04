from abc import ABC, abstractclassmethod

class Pessoa(ABC): 
    @abstractclassmethod #SINALIZA O INTERPRETADOR QUE TODOS OS BLOCOS DE CÓDIGOS SEGUINTES DEVEM SER SOBRESCRITOS EM SUAS CLASSES FILHAS DA HIERARQUIA
    def logar(self):
        pass

class Usuario(Pessoa):
    def logar(self):
        print('Usuário logado no sistema')

class Bot(Pessoa):
    def logar(self, chaveseguranca):
        print('Sistema rodando em segundo plano')



#user1 = Pessoa() # AO INICIALIZAR A CLASSE ABSTRATA 'Pessoa' COM O MÉTODO 'logar', GERA UM ERRO POR CAUSA QUE É UMA CLASSE ABSTRATA (MOLDE)
user1 = Usuario()
user1.logar()