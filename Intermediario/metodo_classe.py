class Pessoa: # CRIAÇÃO DA CLASSE 'Pessoa'
    ano_atual = 2023 # CRIAÇÃO DE OBJETO DE CLASSE 'ano_atual' QUE RECEBE O NÚMERO INTEIRO '2023'

    def __init__(self, nome, idade): # CRIAÇÃO DE UM MÉTODO CONSTUTOR '__init___' QUE RECEBE OS ATRIBUTOS 'nome' E 'idade'
        self.nome = nome # ATRIBUIÇÃO DO DADO 'nome' PARA 'nome'
        self.idade = idade # ATRIBUIÇÃO DO DADO 'idade' PARA 'idade'

    @classmethod #MÉTODO DE CLASSE: UTILIZAÇÃO DE CLASSES ANTERIORMENTE DEFINIDAS COMO ATRIBUTOS
    def ano_nasc(cls, nome, ano_nascimento): # CRIAÇÃO DO MÉTODO 'ano_nasc' O QUAL RECEBE 3 ATRIBUTOS DE CLASSE
        idade = cls.ano_atual - ano_nascimento # CRIAÇÃO DE OBJETO 'idade' QUE RECEBE ATRIBUTO 'cls' [Pessoa.ano_atual] QUE FARÁ SUBTRAÇÃO DO VALOR 'ano_atual'
        return cls(nome, idade) #RETORNA O DADO ACIMA PARA O OBJETO 'idade'

pessoa2 = Pessoa.ano_nasc('André', 1991)

print(pessoa2.idade)