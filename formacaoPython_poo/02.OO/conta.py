class Conta:

    # atributos
    def __init__(self, numero, titular, saldo, limite=1000.0):
        '''
        Criando os atributos PRIVADOS (__) para a classe Conta
        :param numero: numero da conta
        :param titular: nome do titular
        :param saldo: saldo inicial
        :param limite: limite recebe um valor padrão não sendo necessário especificar durante a criação do objeto
        '''
        print(f'Construindo objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @staticmethod
    def codigoBanco():
        return '001'

    @staticmethod
    def codigosBancos():
        return {'BB': '001', 'CAIXA': '104', 'Bradesco': '237'}

    @property
    def saldo(self):
        return self.__saldo

    # getters
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    # setters
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # métodos
    def extrato(self):
        '''
        Método demonstrativo para acessar um atributo da conta
        :return: frase com saldo e nome do titular da conta
        '''
        print(f'Saldo R$ {self.__saldo:.2f} do titular {self.__titular}')

    def depositar(self, valor):
        '''
        Recebe um valor e o acrecenta no saldo da conta
        :param valor: recebe o valor que será acrescentado
        :return: atualiza o valor do saldo
        '''
        self.__saldo += valor

    def __validar_saque(self, valor):
        '''
        Recebe um valor e verifica se este é menor que a soma entre saldo e limite para autorizar o saque
        :param valor: valor a somar com o limite
        :return: True se o valor for menor que a soma, False caso contrário
        '''
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def sacar(self, valor):
        '''
        Subtrai da conta o valor solicitado caso __validar_saque seja True
        :param valor: valor solicitado para saque
        :return: none
        '''
        if self.__validar_saque(valor):
            self.__saldo -= valor
            print('Saque efetuado')
        else:
            print('Saldo insuficiente')

    def transferir(self, valor, contaDestino):
        '''
        Acessa duas contas para fazer uma transferência de valores entre elas
        :param valor: recebe qual o valor será transferido
        :param contaDestino: parâmetro que define qual conta vai receber a transferência
        :return: altera o saldo nas duas contas
        '''
        self.sacar(valor)
        contaDestino.depositar(valor)