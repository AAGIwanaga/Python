import re


mensagem = 'Nãããããããoooooooooo esquecer de pagar a NÃãO mensalidade, não deixar para depois'

print(re.findall(r'não', mensagem, flags = re.I))
print(re.findall(r'nã*o+', mensagem, flags = re.I)) #AMBOS OS METACARACTERES * E + , SEMPRE AO LADO DIREITO DO CARACTER ESCOLHIDO, PEGAM REPETIÇÕES DESSE
print(re.findall(r'não?', mensagem, flags = re.I)) # JÁ O METACARACTERE ? PEGARÁ REPETIÇÃO ENTRE 0 E 1 VEZ
print(re.findall(r'não', mensagem, flags = re.I)) # NÃO ENTENDI O METACARACTERE {}
print(re.findall(r'não', mensagem, flags = re.I))