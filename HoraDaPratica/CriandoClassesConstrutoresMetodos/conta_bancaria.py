class ContaBancaria():
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'

    def __str__(self):
        return f'{self.titular} | {self.saldo} | {self.ativo}'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

conta1 = ContaBancaria('teste1', 1000)
conta2 = ContaBancaria('teste2', 2000)

conta1.alterar_estado()

print(conta1)
print(conta2)