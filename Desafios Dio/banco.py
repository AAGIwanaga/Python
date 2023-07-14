# CRIAÇÃO DO DICIONÁRIO
menu = {
        0 : 'Sair',
        1 : 'Depósito',
        2 : 'Sacar',
        3 : 'Extrato'
}

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

print('O que você deseja fazer? ') # EXIBE AS OPÇÕES DISPONÍVEIS

for chave in menu.items(): # EXIBE AS RELAÇÕES DO DICIONÁRIO
    print(chave)

while True:
    
    opcao = input('Digite a opção desejada: ') #SOLICITA A OPÇÃO DESEJADA

    try: # VALIDA SE A OPÇÃO ESTÁ NA LISTA DE CHAVES DO DICIONÁRIO
        opcao = int(opcao) # SE FOR VALOR INTEIRO, CONTINUA COMO VALOR INTEIRO
    except ValueError: # CASO NÃO SEJA INTEIRO
        opcao = str(opcao) # RETORNA UMA STRING

    if opcao in menu.keys(): # SE OPÇÃO 'chave' SELECIONADA TIVER NO DICIONÁRIO
        print(menu[opcao]) # MOSTRAR A OPÇÃO 'valor'
    else: # CASO CONTRÁRIO
        print('Opção inválida') # MOSTRA OPÇÃO DE ERRO

