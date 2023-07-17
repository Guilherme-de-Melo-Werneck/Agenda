def exibir_menu(): #função que imprime o menu de opções para o usuário
    print("\n---- Lista de Tarefas ----")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def ver_tarefas(tarefas): #imprime as tarefas da lista. Se a lista tarefas estiver vazia, exibe uma mensagem informando que não há tarefas
    print("\n---- Tarefas ----")
    if not tarefas:
        print("Nenhuma tarefa na lista.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas): #função que permite ao usuário adicionar uma nova tarefa à lista
    tarefa = input("\nDigite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def marcar_concluida(tarefas): #função que permite ao usuário marcar uma tarefa como concluída e removê-la da lista
    ver_tarefas(tarefas)
    indice = int(input("\nDigite o número da tarefa concluída: ")) - 1

    if indice >= 0 and indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa marcada como concluída.")
    else:
        print("Índice inválido.")

def remover_tarefa(tarefas): #função que permite ao usuário remover uma tarefa específica da lista
    ver_tarefas(tarefas)
    indice = int(input("\nDigite o número da tarefa a ser removida: ")) - 1

    if indice >= 0 and indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida com sucesso.")
    else:
        print("Índice inválido.")


def funcao(): #solicita ao usuário que digite a opção desejada e, em seguida, executa a ação correspondente chamando as funções apropriadas com base na opção escolhida
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("\nDigite a opção desejada: ")

        if opcao == '1':
            ver_tarefas(tarefas)
        elif opcao == '2':
            adicionar_tarefa(tarefas)
        elif opcao == '3':
            marcar_concluida(tarefas)
        elif opcao == '4':
            remover_tarefa(tarefas)
        elif opcao == '5':
            print("Encerrando o programa")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa.
if __name__ == '__main__':
    funcao()