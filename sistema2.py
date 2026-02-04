def cadastrar():
    nome = input("Nome:")
    idade= input("Idade:")

    with open("pessoas.txt", "a") as arquivo:
        arquivo.write(nome + "," + idade + "\n")

    
    print("Salvo!")


def listar():
    with open("pessoas.txt","r") as arquivo:
        pessoas = arquivo.readlines()

    for pessoa in pessoas:
        print(pessoa.strip())


while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")

    opcao = input("Escolha")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        break

    else:
        print("Opção inválida")