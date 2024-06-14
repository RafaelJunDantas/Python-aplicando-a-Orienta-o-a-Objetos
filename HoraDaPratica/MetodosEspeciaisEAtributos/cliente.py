class Cliente():
    def __init__(self, nome, idade, endereco, telefone):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._telefone = telefone

    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._endereco} | {self._telefone}'

cliente1 = Cliente('A', 1, 'A', 1111)
cliente2 = Cliente('B', 2, 'B', 2222)
cliente3 = Cliente('C', 3, 'C', 3333)

print(cliente1)
print(cliente2)
print(cliente3)