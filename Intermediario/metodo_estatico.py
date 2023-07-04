from random import randint # IMPORTAÇÃO DO MÓDULO 'randint' DA BIBLIOTECA 'random'

class Usuario: # CRIAÇÃO DA CLASSE DE NOME 'Usuario'
    @staticmethod # IDENTIFICAÇÃO, PELO DECORADOR '@' QUE O MÉTODO DE CLASSE É ESTÁTICO (POSSUI O COMPORTAMENTO DE UMA FUNÇÃO INDEPENDENTE)
    def gerador_id(): # DEFINIÇÃO DA FUNÇÃO SEM POSSUIR PARÂMETROS (NÃO RETORNA NADA PARA NENHUM OBJETO DA CLASSE OU DE FORA DELA)
        gerador = randint(100, 999) # CRIA VARIÁVEL GERADOR QUE RECEBE A FUNÇÃO 'randint'
        return gerador # RETORNA O VALOR GERADO PARA A PRÓPRIA VARIÁVEL

print (Usuario.gerador_id()) # EXIBE O VALOR GERADO


