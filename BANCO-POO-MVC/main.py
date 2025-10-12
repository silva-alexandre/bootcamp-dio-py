from Entidade.Menu import Menu
from Entidade.Cliente import Cliente

from Controle.Cliente_controle import Cliente_controle
from Controle.Conta_controle import Conta_controle


def main():
    cliente_controle = Cliente_controle()
    conta_controle = Conta_controle()

    menu_inicial = Menu(
        titulo="Menu Principal",
        opcoes={
            "1": "Iniciar Cadastro",
            "2": "Acessar Cadastro",
            "3": "Sobre o APP?",
            "4": "Sair",
        }
    )

    while True:
        # Exibindo o menu inicial e capturando a escolha do usuário.
        menu_inicial.exibir()
        escolha = input("Escolha uma opção: ")
        # Processando a escolha do usuário.
        if escolha == "1":
            nome = input("Informe seu nome: ")
            data_nascimento = input("Informe sua data de nascimento (DD/MM/AA): ")
            cpf = input("Informe seu CPF: ")
            # Verificando se o CPF já está cadastrado
            if cpf == cliente_controle.validar_cpf(cpf):
                print("CPF já cadastrado. Tente novamente.")
                continue
            # Registrando o cliente em memória e verificando a idade
            cliente = Cliente(nome, data_nascimento, cpf)
            if cliente.verificar_idade():
                cliente = cliente_controle.adicionar_cliente(nome, data_nascimento, cpf)
                # Registando o número da conta e vinculando ao cliente
                numero_conta = f"{len(conta_controle.contas)+1}"
                conta_cliente = conta_controle.adicionar_conta(numero_conta, cliente)
                print(f"Cliente {cliente}, sua conta: {conta_cliente} foi criada com sucesso!")
        #Acessando cadastro já existente
        elif escolha == "2":
            cpf = input("Informe seu CPF para acessar o cadastro: ")
            cliente = cliente_controle.validar_cpf(cpf)
            if cliente and cliente.cpf == cpf:
                print(f"Bem vindo(a) {cliente.nome}!")
                sub_menu = Menu(
                    titulo="Menu de Contas",
                    opcoes={
                        "1": "Exibir resumo da conta",
                        "2": "Depositar",
                        "3": "Sacar",
                        "4": "Exibir extrato",
                    }
                )
                sub_menu.exibir()
                escolha = input("Escolha uma opção: ")
                if escolha == "1":
                    contas = conta_controle.listar_contas()
                    for conta in contas:
                        print(f"Resumo da conta: {conta}, Cliente: {conta.cliente.nome}")
                        break
                elif escolha == "2":
                    conta_controle.depositar(0)
                    conta_controle.exibir_extrato()
                elif escolha == "3":
                    conta_controle.sacar(float(input("Informe o valor a ser sacado: ")))
                    conta_controle.exibir_extrato()
                elif escolha == "4":
                    conta_controle.exibir_extrato()
                else:
                    print("Opção inválida no menu de contas.")
        elif escolha == "3":
            print("App MeuBancoBR - Versão 1.0")
            print("Desenvolvido André Silva")
        
        elif escolha == "4":
            print("Saindo do sistema. Até logo!")
            
        break
        
if __name__ == "__main__":
    main()