#Exercício 8

produtos = []
quantidades = []

while True:
    print("\n--- Menu de Opções ---")
    print("1. Adicionar produto")
    print("2. Realizar entrada no estoque")
    print("3. Realizar saída no estoque")
    print("4. Listar estoque")
    print("0. Sair")
    opcao = input("Opção: ")

    if opcao == '0':
        print("Encerrando o programa...")
        break
    elif opcao == '1':
        if len(produtos) >= 1000:
            print("Limite de produtos atingido!")
        else:
            nome = input("Nome do produto: ")
            produtos.append(nome)
            quantidades.append(0)
            print("Produto adicionado com sucesso!")
    elif opcao == '2':
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            idx = int(input("Número do produto (ID): ")) - 1
            if 0 <= idx < len(produtos):
                qtd = int(input("Quantidade de entrada: "))
                quantidades[idx] += qtd
                print("Entrada realizada com sucesso!")
            else:
                print("Produto inválido.")
    elif opcao == '3':
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            idx = int(input("Número do produto (ID): ")) - 1
            if 0 <= idx < len(produtos):
                qtd = int(input("Quantidade de saída: "))
                if qtd <= quantidades[idx]:
                    quantidades[idx] -= qtd
                    print("Saída realizada com sucesso!")
                else:
                    print("Quantidade insuficiente em estoque.")
            else:
                print("Produto inválido.")
    elif opcao == '4':
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\nEstoque atual:")
            for i in range(len(produtos)):
                print(f"Produto {i+1}: {produtos[i]} - {quantidades[i]} unidades")
    else:
        print("Opção inválida.")
