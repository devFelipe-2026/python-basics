def cadastrar():
    nome = input("Nome: ")
    idade = input("Idade: ")

    with open("pessoas.txt", "a") as arquivo:
        arquivo.write(nome + "," + idade + "\n")

    print("Salvo!")


def listar():
    try:
        with open("pessoas.txt", "r") as arquivo:
            pessoas = arquivo.readlines()

        for pessoa in pessoas:
            print(pessoa.strip())

    except:
        print("Nenhum cadastro ainda.")


def remover():
    nome_remover = input("Digite o nome para remover: ")

    with open("pessoas.txt", "r") as arquivo:
        pessoas = arquivo.readlines()
    
    nova_lista = []

    for pessoa in pessoas:
        if nome_remover not in pessoas:
            nova_lista.append(pessoa)
    
    with open("pessoas.txt", "w") as arquivo:
        for linha in nova_lista:
            arquivo.write(linha)
    
    print("Removido (se existia).")

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Remover")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()
    
    elif opcao == "2":
        listar()

    elif opcao == "3":
        remover()
    
    elif opcao == "4":
        break

    else:
        print("Opção inválida")

