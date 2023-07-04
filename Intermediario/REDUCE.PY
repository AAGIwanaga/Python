from functools import reduce

def soma(num1, num2):
    return num1 + num2

lista = [1,2,3,4,5,6,7,8,9,10]

resultado = reduce(soma, lista)
print(resultado)

print(list(somatoria))