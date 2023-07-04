from itertools import count
contador = count()

for numero in contador:
    print(numero)
    if numero >= 10:
        break


contador2 = count(start = 40, step = 2)

for numero2 in contador2:
    print(numero2)
    if numero2 >= 50:
        break
