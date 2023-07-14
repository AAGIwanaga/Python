class Menu:

    LIMITE_SAQUE = 3
    VALOR_LIMITE = 500
    
    def __init__(self, tela, saldo, extrato, num_saques):
        self.tela = tela
        self.saldo = saldo
        self.extrato = extrato
        self.num_saques = num_saques

    class Deposito(Menu):
        tela = 1
        def __init__(self, val_depos):
            self.val_depos = val_depos
        
        
