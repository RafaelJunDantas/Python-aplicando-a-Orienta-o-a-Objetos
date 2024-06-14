class Restaurante():
    def __init__(self, nome, categoria, endereco, telefone):
        self._nome = nome
        self._categoria = categoria
        self._endereco = endereco
        self._telefone = telefone
        self._ativo = False
    
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._endereco} | {self._telefone} | {"Ativo" if self._ativo else "Inativo"}'
    
restaurante = Restaurante('A', 'B', 'C', '5455')
print(restaurante)