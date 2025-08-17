import sys

modo_de_login = int(input("Olá querido usuário.\nSe você possui uma conta digite [1], caso contrário [2], se deseja sair [3]: "))

if modo_de_login == 1:
    print(" Seja bem-vindo de volta! ") 

elif modo_de_login == 2:
    nome = input("Olá, digite seu nome:\n ")
    dtn = int(input(f"Olá sr {nome}, seja bem-vindo ao JVbank.\nInforme seu ano de nascimento para verificarmos sua idade e se você é válido para ter uma conta (ex: 2005):\n "))
    idade = 2025 - dtn          

    if idade >= 18:
        print(f"Olá sr {nome}, você tem idade válida para criar uma conta!")
    elif idade <= 17:
        print(f"Olá {nome}, você precisa de autorização dos seus pais para isso.")

elif modo_de_login == 3:
    print("Obrigado por usar nosso banco!")
    sys.exit()

else:
    print("Opção inválida! Tente novamente.")
