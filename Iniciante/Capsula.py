class BaseDebase:
    def __init__(self):
        self.__base = {} 
        ''' PODE SER INSTANCIADO COMO:
        SELF.base = A VARIÁVEL base ESTÁ DISPONÍVEL PARA SER INSTANCIADO 
        SELF._base = A VARIÁVEL _base SE TORNA PROTEGIDA, MAS AINDA ACESSÍVEL DE FORA DA CLASSE, MAS IMPLÍCITA
        SELF.__base = A VARIÁVEL __base NÃO ESTARÁ VISÍVEL PARA TODOS E É UM ATRIBUTO DE CLASSEO PROTEGIDO(INACESSÍVEL) E RESTRITO(IMUTÁVEL) SOMENTE A QUEM SABE SUA INSTÂNCIA
        '''

    def inserir(self, nome, fone):
        if 'clientes' not in self.__base:
            self.__base['clientes'] = {nome:fone}
        else:
            self.__base['clientes'].update({nome:fone})
        
    def listar(self):
        for nome, fone in self.__base['clientes'].items():
            print(nome, fone)
        
    def apagar(self, nome):
        del self.__base['clientes'][nome]
    
relClientes = BaseDebase()
relClientes.inserir('Ana', 9913558899)
relClientes.inserir('Fernando', 981252001)
relClientes.inserir('Maria', 999111415)

relClientes.listar()
relClientes.__base = 'Novo Banco de Dados'
print(relClientes.__base)
