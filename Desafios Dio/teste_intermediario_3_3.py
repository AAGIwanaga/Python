filo = {
        'vertebrado' : 1,
        'invertebrado' : 2
}

classe = {
        'ave' : 1,
        'mamifero' : 2,
        'inseto' : 3,
        'anelideo' : 4
}

ordem = {
        'carnivoro' : 1,
        'onivoro' : 2,
        'herbivoro' : 3,
        'hematofago' : 4,
}

animal = {
        'aguia' : '111',
        'pomba' : '112',
        'homem' : '122',
        'vaca' : '123',
        'pulga' : '234',
        'lagarta' : '233',
        'sanguessuga' : '244',
        'minhoca' : '242'
}



def entradas():
    a = filo.get(input())
    b = classe.get(input())
    c = ordem.get(input())
    codigo = f'{a}{b}{c}'
    #print(type(codigo))
    #print(codigo)
    for chave1, valor1 in animal.items():
        if codigo == valor1:
                print(chave1)


    
entradas()



'''for chave in animal.keys():
        print(f'{animal[chave]}')
Animal {chave} e 
def quem():
    #classe = (input()
    #ordem = (input()
    #animal = (input()
    print(type(f'{classe}{ordem}'))
    print(f'{classe}{ordem}{animal}')
    print(f'{classe}{ordem}{animal}')
'''