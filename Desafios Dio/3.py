def analisar_troca(g_comp = int, g_troca = int, total = int): #CRIAÇÃO DA FUNÇÃO COM PARAMETROS 'g_comp' E 'g_troca'
    ab = int(input())

    for a in range(ab):

        g_comp, g_troca = map(int, input().split())
        troca = 0

        while g_comp >= g_troca:
            g_comp = g_comp - g_troca
            troca += 1
        else:
            total = g_comp + troca
            print(total)


    
analisar_troca()



''''
    if isinstance(g_comp, str): # CONDICIONAL VERIFICANDO SE 'g_comp' É STRING
        print("Erro de string") # SE TrUe, RETORNA 'Erro de string'
    elif isinstance(g_comp, float): # CASO 'g_comp' SEJA 'Float'
        print("Erro de float") # SE True, RETORNA 'Erro de float'
    else: # CASO CONTRÁRIO CONTINUA
        pass 
    if isinstance(g_comp, str): # CONDICIONAL VERIFICANDO SE 'g_comp' É STRING
        print("Erro de string") # SE TrUe, RETORNA 'Erro de string'
    elif isinstance(g_comp, float): # CASO 'g_comp' SEJA 'Float'
        print("Erro de float") # SE True, RETORNA 'Erro de float'
    else: # CASO CONTRÁRIO CONTINUA
        pass 
'''