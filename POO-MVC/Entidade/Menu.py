class Menu:
    def __init__(self, titulo, opcoes):
        self.titulo = titulo
        self.opcoes = opcoes
    
    def exibir(self):
        print(self.titulo)
        for chave, valor in self.opcoes.items():
            print(f"{chave}: {valor}")
