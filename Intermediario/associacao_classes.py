class Usuario: #CRIA A CLASSE 'Usuario''
    def __init__(self,nome): # DEFINIE OS PARÂMETROS DA CLASSE PESSOA COM O ATRIBUTO 'nome' (PRIVADA)
        self.__nome = nome
        self.__logar = None

    @property #FUNÇÃO GETTER
    def nome(self): # DEFINIÇÃO DO OBJETO 'nome' COMO PRIVADO 
        return self.__nome

    @property #FUNÇÃO GETTER
    def logar(self): #DEFINIÇÃO DO OBJETO 'logar' COMO PRIVADO
        return self.__logar

    @logar.setter # FUNÇÃO SETTER
    def logar(self, logar): # ??
        self.__logar = logar

class Identificador: #CRIAÇÃO DA CLASSE 'Identificador'
    def __init__(self, numero): #DEFINIÇÃO INICIAL COM O PARAMETRO 'numero'
        self.__numero = numero

    @property # FUNÇÃO GETTER
    def numero(self):
        return self.__numero

    def logar(self): #DEFINIÇÃO DA FUNÇÃO 'logar'
        print('Logando no sistema . . .') # EXIBE A MENSAGEM EM QUESTÃO

usuario1 = Usuario('André') # CRIAÇÃO DA VARIÁVEL 'usuario1' COM ATRIBUIÇÃO DOS CARACTERES 'Andrè' PARA A CLASSE 'Usuario'
identificador1 = Identificador('0001') # CRIAÇÃO DA VARIAVEL 'identificador'' COM ATRIBUIÇÃO DOS CARACTERES '0001' PARA A CLASSE 'Identificador'

usuario1.logar = identificador1 #
usuario1.logar.logar()