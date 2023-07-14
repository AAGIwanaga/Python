menu = [
    {'Opção' : 'd',  'Relação' : 'Depositar', 'Função' : 'opcao_deposito'},
    {'Opção' : 's',  'Relação' : 'Sacar', 'Função' : 'opcao_sacar'},
    {'Opção' : 'e',  'Relação' : 'Extrato', 'Função' : 'opcao_extrato'},
    {'Opção' : 'q',  'Relação' : 'Sair', 'Função' : 'opcao_sair'},
]

menu01 = {}
tela01 = {}

menu_2 = ''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3





def exibir_tela02():
    def opcao_deposito(saldo = 0, extrato = '', erro = 0):
        def validacao_input(saldo = 0, extrato = '', erro = 0):
            valor = input('Informe o valor a ser depositado: ')
            try:
                valor = float(valor)
                return valor
            except:
                valor = str(valor)
                pass
            finally:
                if isinstance(valor, str) is True:
                    print('Caractere informado é "str"')
                else:
                    pass

        valor = float(input('Informe o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor: .2f}'
            print(extrato)
        elif valor == 0:
            print('Não pode depositar 0')
        else:
            print('\nNão é possível depositar um valor negativo,\nPortanto, o valor está sendo convertido para positivo\n')
            valor = abs(valor)
            saldo += valor
            extrato += f'Depósito: R$ {valor: .2f}'
            print(extrato)

    def opcao_sacar():
        valor = float(input('Informe o valor do Saque: '))
        if valor > saldo:
            print('Saldo insuficiente')
        elif valor > limite:
            print('Saque excedeu o limite')
        elif numero_saques >= LIMITE_SAQUES:
            print('Quantidade máxima de saques diário foi alcançada.\nGentileza voltar amanhã')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('O valor informado é invalido')

    def opcao_extrato():
        print(f'''
        ============= EXTRATO =============
        Não foram realizadas movimentações.''' if not extrato else extrato)
        print(f'''
        Saldo: R$ {saldo:.2f}
        ===================================
        ''')

    def opcao_sair():
        print('''
        =========================================
        Obrigado por utilizar os nossos serviços.
        Agradecemos a preferência.
        Volte sempre!
        =========================================
        ''')

    def opca_invalida():
        print('Operação inválida, favor selecionar novamente a operação desejada')



def exibir_tela01():
    def extracao_dados(filtro_chave_1, filtro_valor_1, novo_dicio):
        for item in menu: # SEPARA CADA UM DOS ITEMS DA LISTA 'menu'
            #print(opcao)
            for chave, valor in item.items(): #SEPARA RELAÇÃO CHAVE/VALOR DE DENTRO DE CADA ITEM
                #print(f' [{chave}] : {valor}')
                if chave == filtro_chave_1:
                    #print(valor)
                    chave_extraido = valor
                elif chave == filtro_valor_1:
                    #print(valor)
                    valor_extraido = valor
                else:
                    pass
            dicio = novo_dicio
            dicio.update({chave_extraido : valor_extraido})
        print(dicio.items())

    def tela_inicial():
        x = extracao_dados('Opção', 'Relação', menu01)
        print('Dentre as seguintes opções: ')

        for chave01, valor01 in menu01.items():
            print(f' [{chave01}] : {valor01}')

        entrada = input('Digite a letra entre colchetes: ')

        if entrada not in menu01.keys():
            print('A opção escolhida não está disponível.\n Tente novamente.')

        else:
            print(entrada)
            print('OK')

    def opcao_deposito(saldo = 0, extrato = '', erro = 0):
        def validacao_input(saldo = 0, extrato = '', erro = 0):
            valor = input('Informe o valor a ser depositado: ')
            try:
                valor = float(valor)
                return valor
            except:
                valor = str(valor)
                pass
            finally:
                if isinstance(valor, str) is True:
                    print('Caractere informado é "str"')
                else:
                    pass

        valor = float(input('Informe o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor: .2f}'
            print(extrato)
        elif valor == 0:
            print('Não pode depositar 0')
        else:
            print('\nNão é possível depositar um valor negativo,\nPortanto, o valor está sendo convertido para positivo\n')
            valor = abs(valor)
            saldo += valor
            extrato += f'Depósito: R$ {valor: .2f}'
            print(extrato)

    def opcao_sacar():
        valor = float(input('Informe o valor do Saque: '))
        if valor > saldo:
            print('Saldo insuficiente')
        elif valor > limite:
            print('Saque excedeu o limite')
        elif numero_saques >= LIMITE_SAQUES:
            print('Quantidade máxima de saques diário foi alcançada.\nGentileza voltar amanhã')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('O valor informado é invalido')

    def opcao_extrato():
        print(f'''
        ============= EXTRATO =============
        Não foram realizadas movimentações.''' if not extrato else extrato)
        print(f'''
        Saldo: R$ {saldo:.2f}
        ===================================
        ''')

    def opcao_sair():
        print('''
        =========================================
        Obrigado por utilizar os nossos serviços.
        Agradecemos a preferência.
        Volte sempre!
        =========================================
        ''')

    def opca_invalida():
        print('Operação inválida, favor selecionar novamente a operação desejada')
    
    def switch_tela():
        y = extracao_dados('Opção', 'Função', tela01)
        for chave02, valor02 in tela01.items():
            if chave02 == 'd':
                z = print(valor02)
        
        opcao_deposito(['d'])

        
    
    
    switch_tela()

exibir_tela01()