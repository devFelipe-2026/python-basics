lista = []

while True:
    nome = input("Digite um nome! (ou 'sair'): ")
    idade = int(input('Qual sua idade?'))

    if nome == 'sair':
        break

    lista.append(nome)
    print('Nome adicionado!')

print("lista final")
print(lista)

if idade>= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')




