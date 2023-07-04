carrinho = []
carrinho.append(('Item 1', 30))
carrinho.append(('Item 2', 45))
carrinho.append(('Item 3', 22))
total = 0

for produto in carrinho:
    total = total + produto[1]

total2 = []
for produto in carrinho:
    total2.append(produto[1])

total3 = sum([y for x, y in carrinho])


print('Método tradicional', total) # MÉTODO CONVENCIONAL USANDO LAÇO for PARA LER E SOMAR OS VALORES
print('Usando funções internas', sum(total2)) # MÉTODO UTILIZANDO FUNÇÕES INTERNAS DA LINGUAGEM sum PARA CHEGAR AO MESMO RESULTADO
print('Usando list comprehension', total3) # MÉTODO UTILIZANDO LIST COMPREHENSION
