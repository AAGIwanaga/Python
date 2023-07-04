lista1 = [1,2,3,4,5,6]

for i in lista1:
    print(i * 2) # LAÇO "FOR" NORMAL

lista2 = [i * 2 for i in lista1] # LIST COMPREHENSION: FORMAÇÃO DE UMA LISTA COM USO DE EXPRESSÃOS LÓGICAS E ARITMÉTICAS DIRETAMENTE DENTRO DOS COLCHETES DA FUNÇÃO

print(lista2)

string = '12342567835216541516852476121065816741521329'

comprehension = [letra for letra in string]

print(string[0:20]) # SERÁ LIDO APENAS OS CARACTERES DE 0 A 20

n = 10

comp = [i for i in range(0, len(string), n)]

print(comp)