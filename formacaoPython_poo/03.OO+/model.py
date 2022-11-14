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


class Playlist():
    def __init__(self, nome, listaProgramas):
        self.nome = nome
        self._listaProgramas = listaProgramas

    @property
    def listagem(self):
        return self._listaProgramas

    @property
    def tamanho(self):
        return len(self._listaProgramas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo Mundo em Pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.darLike()
tmep.darLike()
tmep.darLike()
tmep.darLike()
tmep.darLike()
demolidor.darLike()
demolidor.darLike()
atlanta.darLike()
atlanta.darLike()
atlanta.darLike()

listasFilmesSeries = [vingadores, atlanta, demolidor, tmep]

playlistFimDeSemana = Playlist('Fim de Semana', listasFilmesSeries)

print(f'Tamanho da playist: {len(playlistFimDeSemana.listagem)}')

for programa in playlistFimDeSemana:
    print(programa)

print(f'Tá ou não tá? {demolidor in playlistFimDeSemana}')
