# Definindo uma função normal
def soma(a, b):
    return a + b

# Usando uma expressão lambda
soma_lambda = lambda a, b: a + b

print(soma(2, 3))         # SAÍDA DA FUNÇÃO 'soma' : 5
print(soma_lambda(2, 3))  # SAÍDA DA FUNÇÃO ANÔNIMA 'soma_lambda' : 5




variavel1 = lambda n1, n2: n1 * n2

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))



#print(n1)
#print(n2)

print(variavel1(n1,n2))