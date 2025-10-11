from Entidade.Conta import Conta

class Conta_controle:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, numero, cliente):
        conta = Conta(numero, cliente)
        self.contas.append(conta)
        return conta

    def listar_contas(self):
        return self.contas