class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    # getters & setters
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novoNome):
        self._nome = novoNome.title()

    @property
    def likes(self):
        return self._likes

    # métodos
    def darLike(self):
        self._likes += 1


class Filme(Programa):
    # atributos e construtor
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0


class Serie(Programa):
    # atributos e construtor
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0
