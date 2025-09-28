menu = """

[0] Login
[1] Novo cliente

[2] Depositar
[3] Sacar

[4] Extrato
[5] Sair

=> """

AGENCIA ="9090"
LIMITE_SAQUES = 3

clientes = []
contas = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0


while True:

    opcao = input(menu)

    if opcao == "0":
        cpf_login = input("Informe seu CPF:")
        
        cliente_encontrado = None
        
        for cliente in clientes:
            if cliente['cpf'] == cpf_login:
                cliente_encontrado = cliente
                print(f"Seja bem vindo(a) {cliente['nome']}!")

                #Ao realizar o login, o usuário terá acesso a um menu específico.

                login_menu = """
                            [0] Logout - [1] Depositar - [2] Sacar - [3] Extrato
                            [4] Voltar ao menu principal
                            =>  """
                while True:
                    opcao_login = input(login_menu)
                    
                    if opcao_login == "0":
                        print("Logout realizado com sucesso!")
                        break
                    
                    #Opçao de depósito
                    elif opcao_login == "1":
                        valor = float(input("Informe o valor do depósito: "))
                        if valor > 0:
                            saldo += valor
                            extrato += f"Depósito: R$ {valor:.2f}\n"
                            print("Depósito realizado com sucesso!")
                        else:
                            print("Operação falhou! O valor informado é inválido.")
                    #Opção de saque
                    elif opcao_login == "2":
                        valor = float(input("Informe o valor do saque: "))
                        
                        if valor > saldo:
                            print("Operação falhou! Saldo insuficiente.")
                        elif numero_saques >= LIMITE_SAQUES:
                            print("Operação falhou! Número máximo de saques excedido.")
                        elif valor > limite:
                            print("Operação falhou! O valor do saque excede o limite.")
                        elif valor > 0:
                            saldo -= valor
                            extrato += f"Saque: R$ {valor:.2f}\n"
                            numero_saques += 1
                            print("Saque realizado com sucesso!")
                        else:
                            print("Operação falhou! O valor informado é inválido.")
                    #Opção de extrato
                    elif opcao_login == "3":
                        print("\n================ EXTRATO ================")
                        if extrato == "":
                            print("Não foram realizadas movimentações.")
                        else:
                            print(extrato)
                        print(f"\nSaldo: R$ {saldo:.2f}")
                        print("=========================================")
                    # Opção de voltar ao menu principal
                    elif opcao_login == "4":
                        break
                    else:
                        print("Opção inválida, por favor selecione novamente.")

        if not cliente_encontrado:
            print("Cliente não encontrado!")

    #Opção para o novo cliente 
    elif opcao == "1":
        conta = len(contas) + 1
        cpf_cliente = input("Informe seu CPF:")
        cpf_cadastro = False
        for cliente in clientes:
            if cliente['cpf'] == cpf_cliente:
                cpf_cadastro = True
                print("CPF já cadastrado, faça login para acessar sua conta.")
            break
        else:
            nome_cliente = input("Informe seu nome:")
            data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa):")
            numero_conta = conta
            
            #Usando dados do tipo dict para armazenar as informações do cliente e da conta
            novo_cliente = {"nome": nome_cliente, "cpf": cpf_cliente, "data_nascimento": data_nascimento,"agencia": AGENCIA ,"conta": numero_conta}
            nova_conta = {"agencia": AGENCIA, "nome": nome_cliente, "conta": numero_conta}
            
            #Acrescentando os dados nas listas de dict
            clientes.append(novo_cliente)
            contas.append(nova_conta)

            print(f"Cliente {nome_cliente}, sua {conta}  através da agência {AGENCIA} foi cadastrada com sucesso!")

            while True:
                nova_conta_menu = """ [1]Depositar - [2]Saldo - [3]Menu principal   ===>  """

                opcao_nova_conta = input(nova_conta_menu)
                
                if opcao_nova_conta == "1":
                    valor = float(input("Informe o valor do depósito: "))
                    if valor > 0:
                        saldo += valor
                        extrato += f"Depósito: R$ {valor:.2f}\n"
                        print("Depósito realizado com sucesso!")
                    else:
                        print("Operação falhou! O valor informado é inválido.")
                elif opcao_nova_conta == "2":
                    print(f"Seu saldo é de R$ {saldo:.2f}")
                elif opcao_nova_conta == "3":
                    break
            
    elif opcao == "2":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
          saldo += valor
          extrato += f"Depósito: R$ {valor:.2f}\n"
          print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "3":
        valor = float(input("Informe o valor do saque: "))
        
        if valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "4":
        print("\n================ EXTRATO ================")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
    elif opcao == "5":
        print("Obrigado por utilizar nosso serviço!")
        break
    else:
        print("Opção inválida, por favor selecione novamente.")

