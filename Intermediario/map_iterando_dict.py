produtos = [
            {'nome': 'item 1', 'preco' : 32},
            {'nome': 'item 2', 'preco' : 23},
            {'nome': 'item 3', 'preco' : 12},
            {'nome': 'item 4', 'preco' : 10},
            {'nome': 'item 5', 'preco' : 50},
]

# MAP: EXECUTA A FUNÇÃO ESPECIFICADA PARA CADA ITEM DE UMA LISTA/DICIONÁRIO/TUPLA
precos = map(lambda p: p['preco'], produtos) # A EXPRESSÃO FAZ A LEITURA APENAS DOS DADOS/VALORES ATRIBUÍDOS PARA 'preco' DO DICIONÁRIO 'produtos'

for preco in precos:
    print(preco) # LACO for PARA EXIBIR TAIS VALORES

def aumenta_precos(p): # DEFINICAO DE UMA NOVA FUNÇÃO QUE IRÁ
    p['preco'] = p['preco'] * 1.05 # PEGAR O VALOR EXISTENTE EM 'preco' E O MULTIPLICAR POR 1.05
    return p # RETORNA O NOVO VALOR



precos2 = map(aumenta_precos, produtos) # CRIAÇÃO DE UMA NOVA VARIÁVEL QUE CHAMA A FUNÇÃO 'aumenta_precos' E COM A VARIÁVEL DE ONDE OS DADOS SERÃO LIDOS 'produTos')

for produto in precos2: # CRIAÇÃO DE NOVO LAÇO 'for'
    print(produto) # O QUAL EXIBIRÁ O DICIONÁRIO COMPLETO COM OS NOVOS VALORES
