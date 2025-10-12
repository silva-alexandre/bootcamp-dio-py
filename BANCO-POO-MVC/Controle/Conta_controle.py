from Entidade.Conta import Conta

class Conta_controle(Conta):
    def __init__(self):
        self.contas = []
        super().__init__("", None)  # Inicializa a classe base com valores padrão

    def adicionar_conta(self, numero, cliente):
        nova_conta = Conta(numero, cliente)
        self.contas.append(nova_conta)
        return nova_conta
    
    def depositar(self, valor):
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
            return False
        
        return True
    
    def sacar(self, valor):
        saldo = self.saldo
        if valor > saldo:
            print("Saldo insuficiente para saque.")
            return False
        elif valor > 500:
            print("Valor de saque excede o limite diário de R$ 500,00.")
            return False
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True
        
    def exibir_extrato(self):
        print("\n=== Extrato ===")
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for item in self.extrato:
                print(item)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("==============\n")

    def listar_contas(self):
        return self.contas