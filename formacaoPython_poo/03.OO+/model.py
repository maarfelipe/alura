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
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    # atributos e construtor
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.darLike()

atlanta = Serie('atlanta', 2018, 2)
atlanta.darLike()
atlanta.darLike()

listasFilmesSeries = [vingadores, atlanta]

for programa in listasFilmesSeries:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f'{programa.nome} | {detalhes} | {programa.likes}')