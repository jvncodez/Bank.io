import textwrap

def menu():
    menu = """
    ==== MENU ====
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Nova Conta
    [6] Listar Contas
    [0] Sair
    =====================
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("=== Depósito realizado com sucesso! ===")
    else:
        print("=== Operação falhou! Valor informado é inválido. ===")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, nome):
    if valor > saldo:
        print(f"=== Poxa... {nome}, sua operação falhou! Saldo insuficiente. ===")
    elif valor > limite:
        print(f"=== Poxa... {nome}, sua operação falhou! Valor do saque excede o limite. ===")
    elif numero_saques >= limite_saques:
        print(f"=== Poxa... {nome}, sua operação falhou! Número máximo de saques excedido. ===")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("=== Saque realizado com sucesso! ===")
    else:
        print("=== Operação falhou! Valor informado é inválido. ===")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n==== EXTRATO ====")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("====================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Já existe usuário com esse CPF! ===")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print(f"=== Usuário {nome} cadastrado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("=== Usuário não encontrado, fluxo de criação de conta encerrado! ===")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
Agência:\t{conta['agencia']}
C/C:\t\t{conta['numero_conta']}
Titular:\t{conta['usuario']['nome']}
"""
        print("=" * 40)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []
    usuario_logado = None

    while True:
        opcao = menu()

        if opcao == "1":  # Depósito
            if not usuario_logado:
                print("=== Nenhum usuário cadastrado! Crie um usuário e conta antes de depositar. ===")
                continue
            valor = float(input(f"Olá {usuario_logado['nome']}, quanto deseja depositar? "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":  # Saque
            if not usuario_logado:
                print("=== Nenhum usuário cadastrado! Crie um usuário e conta antes de sacar. ===")
                continue
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_de_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_de_saques,
                limite_saques=LIMITE_SAQUES,
                nome=usuario_logado["nome"]
            )

        elif opcao == "3":  # Extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":  # Novo usuário
            criar_usuario(usuarios)

        elif opcao == "5":  # Nova conta
            if not usuarios:
                print("=== Não há usuários cadastrados para criar conta. ===")
                continue
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                usuario_logado = conta["usuario"]

        elif opcao == "6":  # Listar contas
            listar_contas(contas)

        elif opcao == "0":  # Sair
            print("=== Obrigado por usar o JVNBANK! ===")
            break

        else:
            print("=== Operação inválida, tente novamente. ===")

main()
