numeros = (33, 1987, 2020, 19,90, 1000) #TUPLA: DEFINIDO ENTRE PARENTESES
dados = {'Nome': 'Fernando', 'Profissão' : 'Engenheiro'} #DICIONÁRIO: DEFINIDO ENTRE COLCHETES E SEPARADOS COM DOIS PONTOS :



def identificacao(*args, **kwargs):
    print(args)
    print(kwargs)

identificacao(*numeros, **dados)

