class Carro():
    def __init__(self, modelo, cor, ano):
        self._modelo = modelo
        self._cor = cor
        self._ano = ano

    def __str__(self):
        return f'{self._modelo} | {self._cor} | {self._ano}'

carro = Carro('A', 'B', 2)

print(carro)
