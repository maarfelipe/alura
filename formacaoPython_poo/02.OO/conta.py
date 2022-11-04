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

    def sacar(self, valor):
        '''
        Recebe um valor e o diminui do saldo da conta
        :param valor: recebe o valor que será subtraído
        :return: atualiza o valor do saldo
        '''
        self.__saldo -= valor

    def transferir(self, valor, contaDestino):
        '''
        Acessa duas contas para fazer uma transferência de valores entre elas
        :param valor: recebe qual o valor será transferido
        :param contaDestino: parâmetro que define qual conta vai receber a transferência
        :return: altera o saldo nas duas contas
        '''
        self.sacar(valor)
        contaDestino.depositar(valor)

    # getters
    @property
    def saldo(self):
        return self.__saldo

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

#
