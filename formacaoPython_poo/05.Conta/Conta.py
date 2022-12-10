from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta ):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f'Código: {self._codigo}\n' \
               f'Saldo: {self._saldo}'

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3
