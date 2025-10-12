from datetime import datetime

class Cliente:
    def __init__(self, nome, data_nascimento,cpf):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def verificar_idade(self):
        self.data_nascimento = datetime.strptime(self.data_nascimento, "%d/%m/%Y")
        data_atual = datetime.today()
        idade = data_atual.year - self.data_nascimento.year
        if idade > 18:
            print("Bem vindo(a)!")
            return True
        else:
            print("Desculpe, você precisa ser maior de idade para criar uma conta.")
            return False
    
    def __str__(self):
        return f"Cliente(nome={self.nome}, cpf={self.cpf})"