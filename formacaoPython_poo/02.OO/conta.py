class Conta:

    # atributos
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print(f'Construindo objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # metodos
    def extrato(self):
        print(f'Saldo R$ {self.__saldo:.2f} do titular {self.__titular}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor
