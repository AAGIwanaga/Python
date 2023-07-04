lista = [('chave1', 'chave2'), ('chave2', 'valor2'), ('chave3', 'valor3')]

dicionario = {x:y for x, y in lista}
dicionario2 = dict(lista)

print(dicionario) # MÉTODO TRADICIONAL
print(dicionario2) # MÉTODO COMPREHENSION

produtos = [('Caneta', 1.99), ('Lápis', 1.49), ('Caderno', 8.99)]

produtos_com_imposto = {x:y * 1.6 for x, y in produtos}


print('Preços SEM Imposto: ', produtos)
print('Preços COM Imposto: ', produtos_com_imposto)