produtos2 = [
            {'nome': 'item 1', 'preco': 32},
            {'nome': 'item 2', 'preco': 23},
            {'nome': 'item 3', 'preco': 62},
            {'nome': 'item 4', 'preco': 10},
            {'nome': 'item 5', 'preco': 55},
]

def filtra(p):
    if p['preco'] > 50:
        return True

nova_lista3 = filter(filtra, produtos2) # UTILIZAÇÃO DE UMA FUNÇÃO INDEPENDENTE PARA REALIZAR O FILTRO
for produtox in nova_lista3:
    print(produtox)

prod_caro = filter(lambda x: x['preco'] > 50, produtos2) # UTILIZAÇÃO DA FUNÇÃO filter(lambda()) PARA REALIZAR O MESMO FILTRO

print(list(prod_caro))