#Exercício 9

tarefas = []
status = []

while True:
    print("\n--- Menu de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar concluída")
    print("4. Exibir pendentes")
    print("0. Sair")
    opcao = input("Opção: ")

    if opcao == '0':
        print("Encerrando o programa...")
        break
    elif opcao == '1':
        nome = input("Descrição da tarefa: ")
        tarefas.append(nome)
        status.append(False)
        print("Tarefa adicionada com sucesso!")
    elif opcao == '2':
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLista de tarefas:")
            for i in range(len(tarefas)):
                marca = "[X]" if status[i] else "[ ]"
                print(f"{i+1}- {marca} {tarefas[i]}")
    elif opcao == '3':
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            idx = int(input("Número da tarefa para concluir: ")) - 1
            if 0 <= idx < len(tarefas):
                status[idx] = True
                print(f"Tarefa {idx+1} marcada como concluída.")
            else:
                print("Tarefa inválida.")
    elif opcao == '4':
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nTarefas pendentes:")
            for i in range(len(tarefas)):
                if not status[i]:
                    print(f"{i+1}- [ ] {tarefas[i]}")
    else:
        print("Opção inválida.")