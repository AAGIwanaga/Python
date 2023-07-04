string = '654865641654684165414668749321321354618469897415651651651'
n = 10

comp = [i for i in range(0, len(string), n)] # LEITURA DO COMPRIMENTO, PULANDO DE n EM n CARACTERES
comp2 = [(i, i + n ) for i in range (0, len(string), n)] # LEITURA DO COMPRIMENTO DE CARACTERE [0:n] AO PRÓXIMO [n:2n]
comp3 = [string[i:i + n] for i in range(0, len(string), n)] # EXTRAÇÃO DOS DADOS ENTRE OS CARACTERES [0:n], [n:2n]

lista = [string[i:i + n] for i in range(0, len(string), n)] # CRIAÇÃO DE UMA VARIÁVEL DE NOME lista QUE REALIZA O FATIAMENTO DOS DADOS LIDOS ANTERIORMENTE
retorno = '.'.join(lista) # CRIAÇÃO DE OUTRA VARIÁVEL DE NOME retorno QUE PEGA OS DADOS DA VARIÁVEL LISTA E CONCATENA COM O CARACTERE .

print(comp) # INTERVALO A SER LIDO
print(comp2) # INTERVALO DOS ELEMENTOS DE QUAL EM QUAL
print(comp3) # ELEMENTOS FATIADOS EM SI
print(retorno) # ELEMENTOS CONCATENADOS DA VARIÁVEL retorno