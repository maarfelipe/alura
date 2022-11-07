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

    def __str__(self):
        return f'{self.nome:<30} | {self.ano} | {self.likes} Likes'


class Filme(Programa):
    # atributos e construtor
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome:<30} | {self.ano} | {self.duracao:<3} | {self.likes} Likes'


class Serie(Programa):
    # atributos e construtor
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome:<30} | {self.ano} | {self.temporadas:<3} | {self.likes} Likes'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.darLike()

atlanta = Serie('atlanta', 2018, 2)
atlanta.darLike()
atlanta.darLike()

listasFilmesSeries = [vingadores, atlanta]

for programa in listasFilmesSeries:
    print(programa)