import re

minha_string = 'Fernando fernandou na fernanda fernandada chegará a meia noite.'
print(re.findall(r'fernand.', minha_string.lower())) #O CARACTERE PONTO É UTILIZADO COMO UM CARACTERE CORINGA LEMBRANDO QUE A LINGUAGEM PYTHON É SENSÍVEL AOS CARACTERES
print(re.findall(r'FERNANDO|FERNANDA', minha_string.upper())) # O CARACTERE | SERIA O EQUIVALENTE A UMA ALTERNATIVA INCLUSIVA "OU" 
print(re.findall(r'[fF]', minha_string.upper())) # PARA NÃO PRECISAR UTILIZAR A OPÇÃO PIPE INFINITAMENTE, PODE-SE UTILIZAR OS CARACTERES DESEJADOS ENTRE COLCHETES
print(re.findall(r'[a-zA-Z]', minha_string.upper())) #ESSA FUNÇÃO AINDA É QUASE COMO SE FOSSE EQUIVALENTE AO CONJUNT [a-z],  [1-87], [a-zA-Z]
print(re.findall(r'FERNAND.', minha_string, flags = re.I)) # NESTA SITUAÇÃO, É POSSÍVEL UTILIZAR O TERCEIRO PARAMETRO FLAGS, PARA IGNORAR O FORMATO DOS CARACTERES

#''' LEMBRANDO QUE A LINGUAGEM PYTHON É SENSÍVEL AOS CARACTERES'''

#print(minha_string.lower())