lista = [1,2,3,4,5,6,7,8,9,10]

#FUNÇÃO map: REALIZA UMA ITERAÇÃO SOBRE ALGUM ELEMENTO EM ESPECÍFICO DE UMA LISTA OU DICIONÁRIO
nova_lista = map(lambda x: x * 2, lista)

#mesmo que:
nova_lista2 = [x * 2 for x in lista]

print(lista)
print(list(nova_lista))

print(nova_lista2)