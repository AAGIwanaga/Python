""" CRIAÇÃO DE FUNÇÕES
1) UTILIZAR A FUNÇÃO def XX():
    CÓDIGO DA FUNÇÃO
2) SUA FUNÇÃO ESTÁ CRIADA E JÁ PODE CHAMÁ-LA
3) *args    :PERMITE QUE A FUNÇÃO UTILIZE VARIÁVEIS EM FORMA DE LISTA
4) **kwargs :PERMITE QUE A FUNÇÃO UTILIZE VARIÁVEIS EM FORMA DE DICIONÁRIO


"""

def boas_vindas():
    print(f"Salve, boas vindas, seu otário!\n" "Espero que você se foda bastante, aqui!")

def boas_vindas_nome(nome):
    print(f"{nome}, espero que você se arrependa bastante!")


print(boas_vindas_nome(nome))


"""def quadrado(*num):
    for par in num:
        result = par * num
    return(result)

num = quadrado(3, 3, 4)

print(num)
"""