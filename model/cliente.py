from model.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade, sexo, cpf, endereco):
        super().__init__(nome, idade, sexo, cpf)
        self.endereco = endereco

    def getCliente(self):
        return self.nome, self.idade, self.sexo, self.cpf, self.endereco

    def setCliente(self, nome, idade, sexo, cpf, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.endereco = endereco

