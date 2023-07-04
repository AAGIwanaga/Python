def conversor_num(num): # DEFINIÇÃO DE UMA FUNÇÃO COM UM PARÂMETRO
    try: # O CÓDIGO IRÁ TENTAR REALIZAR A SEGUINTE OPERAÇÃO
        num = int(num) # VALIDAR SE O PARÂMETRO É UM NÚMERO INTEIRO
        return num # CASO POSITIVO, RETORNA O PRÓPRIO VALOR
    except ValueError: # CASO NÃO SEJA UM VALOR INTEIRO
        #try: # IRÁ FAZER UMA OUTRA TETATIVA
        num = float(num) # VERIFICAR SE O PARÂMETRO É UM 'float'
        return num # CASO POSITIVO, RETORNA O PRÓPRIO VALOR
        #except ValueError: ESTA EXCEÇÃO SERIA NECESSÁRIA CASO NÃO TIVESSE A FUNÇÃO 'finally' JUNTO COM O 'pass'
            #pass: 
    finally:
        print('Você digitou um caractere que não pode ser convertido')
    
num1 = conversor_num(input('Digite um número: '))

if num1 is not None:
    print(num1 + 100)
#else:
    #print('Operação inválida.') ESTA PARTE TAMBÉM PODE SER DESCARTADA, POR CAUSA DO 'finally'


'''
ESTE EXEMPLO INICIA NA PÁGINA 486 'TRY, EXCEPT' '''