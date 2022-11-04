class Cliente:

    # atributos
    def __init__(self, nome):
        self.__nome = nome

    # getters
    @property
    def nome(self):
        print('Chamado @property nome()')
        return self.__nome.title()

    # setters
    @nome.setter
    def nome(self, nome):
        print('Chamando setter nome()')
        self.__nome = nome
