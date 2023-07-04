from random import randint

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade, login = False, logoff = False):
        self.nome = nome
        self.idade = idade
        self.login = login
        self.logoff = logoff
    
    def logar(self):
        if self.login:
            print(f'{self.nome} já está logado no sistema.')
            return
        
        print(f'Bem vindo {self.nome}, você já está logado no sistema.')
        self.login = True

    @staticmethod
    def gerador_id():
        gerador = randint(100, 999)
        return gerador

    def deslogar(self):
        if not self.login:
            print(f'{self.nome} não está logado no sistema.')
            return
        print(f'{self.nome} foi deslogado do sistema.')
        self.login = False

    @classmethod
    def ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


pessoa2 = Pessoa.ano_nascimento('André', 1991)

print(pessoa2.gerador_id())
#print(pessoa2.idade)
#usuario.logar()
#usuario.logar()
#usuario.deslogar()