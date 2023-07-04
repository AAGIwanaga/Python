idade = int(input('Digite sua idade: '))

if idade <= 0:
    raise Exception('Idade inválida!!!') # É UM MÉTODO DE LEVANTAR UM ERRO DE FORMA REDUZIDA.

print(f'Você tem {idade} anos!!!')