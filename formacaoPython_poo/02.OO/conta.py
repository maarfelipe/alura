class Conta:

    # atributos
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print(f'Construindo objeto ... {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    # metodos
    def extrato(self):
        print(f'Saldo R$ {self.saldo:.2f} do titular {self.titular}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
