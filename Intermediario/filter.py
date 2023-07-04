'''
FUNÇÃO map: REALIZA UMA ITERAÇÃO SOBRE ALGUM ELEMENTO EM ESPECÍFICO DE UMA LISTA OU DICIONÁRIO
FUNÇÃO filter: SEMELHANTE COM A FUNÇÃO map, SÓ QUE UTILIZA UMA FUNÇÃO CONDICIONAL ('True') COMO FILTRO

idosos = NOVA VARIÁVEL
filter = FUNÇÃO DE ITERAÇÃO DE TODOS OS ELEMENTOS DE UMA LISTA/DICIONÁRIO/TUPLA 
lambda = FUNÇÃO ANÔNIMA (SEM UM NOME DEFINIDO), A QUAL PODE REALIZAR OPERAÇÕES ARITMÉTICAS
lambda argumentos: expressão
            ARGUMENTO 'x', EXPRESSÃO [SENDO x O VALOR ['idade'] QUE É MAIOR DO QUE O VALOR 70]
COMO A FUNÇÃO lambda ESTÁ DENTRO DA FUNÇÃO filter, AQUELA REALIZARÁ A EXPRESSÃO PARA TODOS OS ITEMS DO DICIONÁRIO
'''


pessoas = [
            {'nome': 'Ana', 'idade': 22},
            {'nome': 'Maria', 'idade': 72},
            {'nome': 'Paulo', 'idade': 55},
            {'nome': 'Pedro', 'idade': 68},
            {'nome': 'Rafael', 'idade': 99},
            {'nome': 'Tania', 'idade': 18},
]

idosos = filter(lambda x: x['idade'] > 70, pessoas)

print(list(idosos))

