""" Listas:  
1) OS ITENS INSERIDOS NELAS SÃO DINÂMICAS 
2) NÃO SE PODE INSERIR 2 ITENS IGUAIS
3) EM LISTA SE USA COLCHETE
4) CASO QUEIRA RETIRAR O ÚLTIMO ITEM MAIS A DIREITA, USAR O COMANDO .POP
5) PARA SE CONSULTAR A QUANTIDADE DE ITENS USAR O COMANDO LEN()
"""


lista1 = [1, 5, 'Jão', 'Maria']
lista1.append(2) #adicionei o item '2' à lista
lista1.append(2)
lista1.remove('Jão') # Removi o item 'Jão' da lista
del lista1[0] #deletei o item de posição 0/primeiro da lista


print(lista1)

lista1.reverse()

print(lista1)
print(len(lista1))



""" Tuplas:  
1) OS ITENS INSERIDOS EM UMA TUPLA SÃO PRÉDEFINIDOS E IMUTÁVEIS
2) EM UMA TUPLA USA-SE PARENTESES
3) SE TIVER APENAS UM ELEMENTO, É NECESSÁRIO COLOCAR ESPECIFICAÇÃO TUPLE OU COLOCAR UM SEPARADOR VIRGULA, MESMO NÃO HAVENDO SEGUNDO ELEMENTO
"""

tuplinha1 = tuple('1')
tuplinha2 = (1, )
tuplinha3 = (1, 2)


print(tuplinha1)

""" DICIONÁRIOS:
1) ORGANIZADOR DE DADOS EM FORMATO {CHAVE : VALOR}
2) UTILIZAÇÃO DO CARACTERE CHAVE {}
3) RECOMENDÁVEL UTILIZAR TABULAÇÃO VISIVELMENTE ORGANIZADO
4) PARA SEPARAR OS ELEMENTOS, UTILIZAR VIRGULA
5) CONSULTA DE 1 VALOR .GET()
6) CONSULTA DE CHAVES .KEY()
7) CONSULTA DE VALORES .VALUES()
8) CONSULTA DE TUDO .ITEMS()
"""

dic = { 'nome' : 'André', 
        'idade' : '31', 
        'formacao' : 'administrador'}

print(dic)
print(len(dic))
print(dic.get('nome'))
print(dic.keys()) #retorna as chaves do dicionário
print(dic.values()) #retorna os valores contidos no dicionário
print(dic.items()) # retorna a relação chave valor


""" CONJUNTO:
1) POSSUI SINTAXE DE DICIONÁRIO {} , MAS É APENAS UM CONJUNTO DE DADOS ALINHADOS
2) CONJUNTO SÓ PODE TER NÚMEROS
3) CONSULTA A UNIÃO 2 CONJUNTOS .UNION()
4) CONSULTA A INTERESECÇÃO .INTERSECTION()
5) PARA ATUALIZAR O CONJUNTO, UTILIZAR O COMANDO UPDADE
6) CONSULTA SE UM CONJUNTO PERTENCE A OUTRO "<=" OU ">="
7) REALIZAR A DIFERENÇA DOS CONJUNTOS "-" RETORNANDO TRUE OR FALSE
"""
conj1 = {1, 2, 5}
conj2 = (2, 4, 9)

conj1.union(conj2)
conj1.update(conj2)
print(conj1)

#print(conj1)