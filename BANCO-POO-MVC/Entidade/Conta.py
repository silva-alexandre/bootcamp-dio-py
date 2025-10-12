class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = []
        
    def __str__(self):
        return f"Conta {self.numero})"
