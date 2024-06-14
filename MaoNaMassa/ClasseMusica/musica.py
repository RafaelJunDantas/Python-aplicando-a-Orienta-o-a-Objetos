class Musica():
    def __init__(self, nome, artista, duracao):
        self._nome = nome
        self._artista = artista
        self._duracao = duracao # segundos

    def __str__(self):
        return f'Musica: {self._nome} | Artista: {self._artista} | Duracao: {self._duracao}'

musica1 = Musica('teste', 'teste', 60)
musica2 = Musica('KURA KURA', 'ADO', 192)
musica3 = Musica('うっせぇわ', 'ADO', 205)

print(musica1)
print(musica2)
print(musica3)