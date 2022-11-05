class Filme:
    # atributos e construtor
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    # getters & setters
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome.title()

    @property
    def likes(self):
        return self.__likes

    def darLike(self):
        self.__likes += 1


class Serie:
    # atributos e construtor
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = temporadas
        self.__likes = 0

    # getters & setters
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome.title()

    @property
    def likes(self):
        return self.__likes

    def darLike(self):
        self.__likes += 1
