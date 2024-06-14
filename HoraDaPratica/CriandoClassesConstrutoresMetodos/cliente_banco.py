from conta_bancaria import ContaBancaria

class ClienteBanco():
    def __init__(self, nome, idade, endereco, cpf, email, saldo):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._cpf = cpf
        self._email = email
        self.criar_conta(saldo)

    def __str__(self):
        return f'{self._nome}, {self._idade}, {self._endereco}, {self._cpf}, {self._email}'
    
    def print_conta(self):
        return self._conta_bancaria
    
    def alternar_status_conta(self):
        self._conta_bancaria.alterar_estado()

    def criar_conta(self, saldo):
        self._conta_bancaria = ContaBancaria(self._nome, saldo)

cliente1 = ClienteBanco('teste', 1, 'teste', 'teste', 'teste', 1000)

cliente1.alternar_status_conta()

print(cliente1.print_conta())