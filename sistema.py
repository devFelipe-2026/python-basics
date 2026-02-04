while True:
    print('\n1 - Cadastrar')
    print('2 - Listar')
    print('3 - Sair')

    opcao = input("Escolha ")

    if opcao == "1":
        nome = input("nome: ")
        idade = input("idade: ")

        with open("pessoas.txt", 'a') as arquivo:
            arquivo.write(nome + "," + idade + "\n")

            print("Salvo!")
    
    elif opcao == "2":
        with open("pessoas.txt", "r") as arquivo:
            pessoas = arquivo.readlines()

        for pessoa in pessoas:
            print(pessoa.strip())
        
    elif opcao == "3":
        break

    else:
        print("opção inválida")
