from modelos.avaliacao import Avaliacao

class Restaurante():

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    @property
    def ativo(self):
        return "Ativo" if self._ativo else "Inativo"
    
    def __str__(self):
        return f'{self._nome.ljust(20)} | {self._categoria.ljust(20)} | {str(self.media_avaliacoes).ljust(20)} | {self.ativo}'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def adicionar_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliacoes'
        media = sum(avaliacao._nota for avaliacao in self._avaliacao) / len(self._avaliacao)
        return round(media, 1)

    @classmethod
    def listar_restaurantes(cls):
        print('Listando os restaurantes:')
        print(f'{"Nome".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliacao".ljust(20)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante}')

