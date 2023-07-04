class Produto: # CRIAÇÃO DA CLASSE PRODUTO
    def __init__(self, nome, preco = 0): # CRIAÇÃO DO MÉTODO CONSTRUTOR '__init__' O QUAL RECEBE OS PARAMETROS 'nome' E 'preco' DEFINIDO INICIALMENTE COMO ZERO
        self.nome = nome # CRIAÇÃO DO OBJETO 'nome'
        self.preco = preco # CRIAÇÃO DO OBJETO 'preco'
    
    def aplica_desconto(self, percentual): # CRIAÇÃO DO MÉTODO DE CLASSO 'aplica_desconto', O QUAL RECEBERÁ O OBJETO 'percentual'
        self.preco = self.preco - (self.preco*(percentual/100)) # PEGA O OBJETO 'preco' E APLICA UMA FÓRMULA DE DESCONTO

    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self, preco_validado):
        if isinstance(preco_validado, str):
            preco_validado = float(preco_validado.replace('R$', ''))
        self._preco = preco_validado

produto1 = Produto('Camiseta', 99)
produto1.aplica_desconto(5)
print(produto1.preco)

produto2 = Produto('Calça', 'R$59')
produto2.aplica_desconto(15)
print(f'Produto2 após aplicação do desconto terá valor de {produto2.preco}')