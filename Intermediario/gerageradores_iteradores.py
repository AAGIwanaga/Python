import sys

from itertools import zip_logest


def gera_numero():
    num = 0
    while True:
        yield num
        num += 1

gerador = gera_numero()

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

cidades = ['Porto Alegre', 'Curitiba', 'Salvador', 'Belho Horizonte', 'Rio de Janeiro', 'Goiânia']
estados = ['RS', 'PR', 'BH', 'MG']

cidades_estados = zip_longest(cidades, estados)
cidades_estados2 = zip_logest(cidades, estados, fillvalue = 'Desconhecido')

print(type(cidades_estados))

for i in cidades_estados:
    print(i)