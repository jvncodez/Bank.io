Nome = str(input("Olá Usuario, seja bem vindo, poderia informar seu nome e sobrenome? ex: Paulo Santos \n "))

print(f"Olá {Nome.strip()}. Seja bem vindo ao JvnBank!")

Menu="""
============= JVNBANK =============
      ECOLHA A OPÇÃO DESEJADA
      [1]DEPOSITAR
      [2]SACAR
      [3]EXIBIR EXTRATO
      [0]SAIR

===================================
"""
Saldo = 1000
Extrato = ""


while True:
    
    Opcao = int(input(Menu)) 

    if Opcao  ==  1:
        Valor = float(input(f"Olá {Nome.strip()} Quanto você deseja depositar? "))
        Saldo += Valor
        Extrato += f"Realizou um deposito no valor de R$ {Valor:.2f} \n "  
        print(f" Olá Seu Saldo atual é de {Saldo:.2f}")

    elif Opcao == 2: 

        Valor =  float(input("Escolha o Valor que voce deseja sacar!"))
        if Valor > Saldo:
            print(f"Escolha Outro valor seu saldo atual é de {Saldo} \n ")
        else:
            Saldo -= Valor
            Extrato += f" Realizou um Saque no Valor de R$ {Valor:.2f} \n "  
            print(f"Saque realizado com sucesso, seu saldo atual é de R$ {Saldo}")

    elif Opcao == 3:
        print(""" \n ================== EXTRATO ================== """)

        if Extrato == "":
            print("Nenhuma movimentação financeira")
        else:
            print(f"Olá {Nome.strip()} Aqui está seu Extrato Bancario! \n {Extrato}")

    elif Opcao == 0:
        print(f"Até a proxima, {Nome.strip()} Obrigado por Utilizar nosso sistema financeiro")
        break

    else:
        print(f"{Nome.strip()} essa opção é invalida.")
    

        

  
         
            
          
       
        

            
