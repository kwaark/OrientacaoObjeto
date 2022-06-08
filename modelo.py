class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes
    def dar_like(self):
        self._likes += 1
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = nome.title()
    def __str__(self):
        return f'{self._nome} - {self.ano } - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return f'{self._nome} - {self.duracao} min - ano {self.ano } - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
        return f'{self._nome} - {self.temporadas} temporadas - ano {self.ano } - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme('Vingadores - Guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme ('todo mundo em pânico', 1999, 100)
cdl = Filme('clube da luta', 1999, 239)
vikings = Serie('vikings', 2015, 6)

vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
vikings.dar_like()
vikings.dar_like()
vikings.dar_like()
cdl.dar_like()
cdl.dar_like()
cdl.dar_like()
cdl.dar_like()

filmes_e_series = [vingadores, atlanta, tmep, cdl, vikings]
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

len(playlist_fim_de_semana)

for programa in playlist_fim_de_semana.listagem:
    print(programa)




