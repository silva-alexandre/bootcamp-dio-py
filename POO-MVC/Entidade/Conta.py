class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente

    def __str__(self):
        return f"Conta {self.numero})"
