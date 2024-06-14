class Livro():

    livros = []

    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicado} | {self.disponivel}'
    
    @property
    def disponivel(self):
        return 'Diponivel' if self._disponivel else 'Indisponivel'
    
    def emprestar(self):
        self._disponivel = not self._disponivel

    @classmethod
    def verificar_diponibilidade(cls, ano):
        for livro in cls.livros:
            if livro._disponivel and livro._ano_publicado == ano:
                print(livro)
    

livro1 = Livro('teste', 'teste', 2000)
livro2 = Livro('bom dia', 'bom dia', 1000)
livro3 = Livro('aaaaaaaa', 'aaaaaaaa', 2000)

livro1.emprestar()

print(livro1)
print(livro2)
print(livro3)

print('-' * 50)

Livro.verificar_diponibilidade(2000)