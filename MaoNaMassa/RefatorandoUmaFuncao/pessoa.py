class Pessoa():
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    @property
    def saudacao(self):
        return f'Sua profissao e {self._profissao}' if self._profissao == 'teste' else f'{self._profissao.title()} e a sua profissao'

    def __str__(self):
        return f'{self._nome.ljust(15)} | {self.saudacao.ljust(20)} | {self._idade}'
    
    def aniversario(self):
        self._idade += 1

pessoa1 = Pessoa('a', 1, 'a')
pessoa2 = Pessoa('teste', 0, 'teste')

print(pessoa1)
print(pessoa2)
print('-' * 50)
