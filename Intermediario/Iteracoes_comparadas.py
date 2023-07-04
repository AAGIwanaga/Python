estoque = [
            {'Item01': 'Camisa Nike', 'Preco': 39.90},
            {'Item02': 'Camisa Adidas', 'Preco': 37.90},
            {'Item03': 'Moletom 00', 'Preco': 79.90},
            {'Item04': 'Calça Jeans', 'Preco': 69.90},
            {'Item05': 'Tenis AllStar', 'Preco': 59.90},
]



# MÉTODO CONVENCIONAL PARA EXTRAIR DADOS
precos01 = [] # CRIAÇÃO DE UMA VARIÁVEL QUE RECEBE COMO ATRIBUTO UMA LISTA VAZIA
for preco in estoque: # CRIAÇÃO DE UM LAÇO 'for' QUE PERCORRE CADA ELEMENTO DO DOCIONÁRIO 'estoque'
    precos01.append(preco['Preco']) # PERCORRENDO OS ELEMENTOS, ELE ADICIONARÁ APENAS OS VALORES DAS CHAVES 'Precos'
print(f'Preços de estoque (normal) {precos01}') #EXIBE A MENSAGEM 'Preços de estoque (normal) com seus reespectivos preços.



# EXTRAINDO DADOS VIA 'map' + FUNÇÃO 'lambda'
precos02 = list(map(lambda p: p['Preco'], estoque)) # CRIAÇÃO DA VARIÁVEL 'precos02' QUE RECEBE ATRIBUÍDO PARA SI UMA 'list' QUE FAZ USO DA FUNÇÃO 'map' PARA,
                                                    # QUE COM A FUNÇÃO 'lambda', EXTRAIR OS VALORES DE 'Preco' DA BASE DE DADOS 'estoque'
for preco in precos02: #CRIAÇÃO DE UM LAÇO 'for' PARA:
    print(preco) # EXIBIR APENAS OS DADOS QUE QUEREMOS, QUE NESTE CASO É 'preco'
print(f'Preços de estoque (Map + Lambda) {precos02}') #



# EXTRAINDO DADOS VIA LIST COMPREHENSION
precos03 = [preco['Preco'] for preco in estoque] #CRIAÇÃO DA VARIÁVEL 'preco03', A QUAL RECEBE APENAS OS ITENS 'preco' DA LISTA 'estoque'
print(f'Preços de estoque (List Comprehension) {precos03}') #EXIBIR A MENSAGEM COM OS VALORES



# EXTRAINDO DADOS VIA 'filter'
precos04 = list(filter(lambda p: p['Preco'] >= 60, estoque)) # CRIAÇÃO DA VARIAVEL 'precos04' QUE RECEBE ATRIBUTO DA LISTA 'estoque'
                                                             # COM FILTRO QUE EXTRAI VALORES >= 60, COM O AUXÍLIO DA FUNÇÃO 'lambda'
print(f'Preços de estoque (Filters) {precos04}') # EXIBE A MENSAGEM COM OS VALORES



# COMBINANDO 'filter' E LIST COMPREHENSION
precos05 = [preco['Preco'] for preco in estoque if preco['Preco'] > 60] # CRIAÇÃO DA VARIÁVEL 'preco05' QUE RECEBE A LISTA CRIADA DO LAÇO 'for'
                                                                        # O QUAL PERCORRE OS DADOS DE 'estoque', VALORES 'Preco'
                                                                        # AINDA É COLOCADA UMA CONDICIONAL PARA RETORNAR APENAS OS VALORES > 60
print(f'Preços de estoque (Filter + List Comprehension) {precos05}') # EXIBE A MENSAGEM COM OS VALORES



# COMBINANDO 'map' E 'filter'
precos06 = list(map(lambda p: p['Preco'],                   # CRIAÇÃO DA VARIÁVEL 'precos06' QUE RECEBE UMA LISTA QUE FAZ USO DO 'map', ONDE O PRIMEIRO ELEMENTO É
                    filter(lambda p: p['Preco'], estoque))) # A FUNÇÃO 'lambda' A QUAL PERCORRE E RETORNA OS VALORES DE 'Preco' COMO SEGUNDO ELEMENTO DO MAPEAMENTO 'filter'
                                                            # ESTA QUE REALIZA O MESMO PROCEDIMENTO EXTRAINDO DADOS DO ESTOQUE
print(f'Preços de estoque (Map + Filter) {precos06}')


# EXTRAINDO DADOS VIA 'Reduce'
from functools import reduce #IMPORTAÇÃO DA FUNÇÃO 'reduce' DA BIBLIOTECA 'functools'
def func_reduce(soma, valores): # É CRIADA A FUNÇÃO 'func_reduce' QUE RECEBE 2 ARGUMENTOS 'soma' E 'valores'
    return soma + valores['Preco'] # 'valores' RECEBERÁ OS ATRIBUTOS DE 'Preco', 'soma' RECEBERÁ O RESULTADO DA FUNÇÃO
precos_total = reduce(func_reduce, estoque, 0) # 'reduce(função, lista, opcional) RETORNA UM ITERÁVEL A UM ÚNICO VALOR 'opcional' = SOMA COMECE DO 0
print(f'Soma dos Preços (Reduce) {precos_total}')


# EXTRAINDO COM 'Reduce' E LIST COMPREHENSION
from functools import reduce #IMPORTAÇÃO DA FUNÇÃO 'reduce' DA BIBLIOTECA 'functools'
precos_total = reduce(lambda soma, valores: soma + valores['Preco'], estoque, 0) # CRIADA A VARIÁVEL 'precos_total' QUE RECEBE 'reduce' COM OS SEGUINTES PARÂMETROS:
                                                                                 # 'soma' = SOMA DOS RESULTADOS; 'valores' = ITENS 'Preco'; DO DICIONÁRIO 'estoque' DO 0
print(f'Soma dos Preços (Reduce + List Comprehension) {precos_total}')


# REDUCE(MÉTODO OTIMIZADO)
from functools import reduce #IMPORTAÇÃO DA FUNÇÃO 'reduce' DA BIBLIOTECA 'functools'
precos_total1 = sum([preco['Preco'] for preco in estoque]) # CRIADA A VARIÁVEL 'precos_total1' QUE RECEBE FUNÇÃO 'sum' QUE RECEBE O PARÂMETRO 'preco' COM OS VALORES ['Preco']
                                                           # FORMANDO LAÇO 'for' QUE RECEBE APENAS OS ITENS 'preco' DA LISTA 'estoque'
print(f'Soma dos Preços (Reduce Otimizado) {precos_total1}')