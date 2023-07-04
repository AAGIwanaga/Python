
def pessoa1 (nome, idade, funcao):
    print(f'{nome} tem {idade} anos, função: {funcao}.')

def pessoa2(nome, idade = 18, funcao = 'técnico'):
    print(f'{nome} tem {idade} anos, função: {funcao}.')

p1 = pessoa1('Fernando', 18, funcao = 'gerente')
p2 = pessoa2('André', funcao = 'Administrador')

#print(p1.idade)
p2
