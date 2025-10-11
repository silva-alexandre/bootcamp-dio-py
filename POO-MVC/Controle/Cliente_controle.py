from Entidade.Cliente import Cliente

class Cliente_controle:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, nome, data_nascimento, cpf):
        cliente = Cliente(nome, data_nascimento, cpf)
        self.clientes.append(cliente)
        return cliente

    def listar_clientes(self):
        return self.clientes

    def validar_cpf(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente