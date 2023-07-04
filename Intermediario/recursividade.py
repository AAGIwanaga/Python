def fatorial(num: int) -> int: 
    '''RECURSIVIDADE: A FUNÇÃO PODE SER REUTILIZADA INÚMERAS VEZES CONFORME A DEMANDA
    PODENDO RETORNAR A PRÓPRIA FUNÇÃO REPROCESSANDO OS DADOS'''


    if num ==1:
        return 1
    #print(num)
    #print(fatorial)
    return num * fatorial(num - 1)

fator = fatorial(4)
print(fator)