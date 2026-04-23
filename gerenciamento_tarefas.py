tarefas = []
def main():
    print("Bem vindo ao Sistema de Gerenciamento de Tarefas. ")
    while True:
        print("\nMenu:")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Marcar Tarefa como Concluída.")
        print("4. Remover Tarefa")
        print("5.Sair")


        escolha = input("Digite o número que corresponde a opção desejada: ")

        if escolha == "1":
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(descricao)
        elif escolha == "2":
            visualizar_tarefas()
        elif escolha == "3":
            visualizar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa que você deseja marcar como concluída: ")) -1
                marcar_tarefa(indice)
            except ValueError:
                print("Entrada inválida! Por favor digite um número: ")
        elif escolha == "4":
            visualizar_tarefas()
            try:
                indice = int(input("Digite o índice que deseja remover"))-1
                remover_tarefa(indice)
            except ValueError:
                print("Entrada inválida! Por favor digite um número: ")

        elif escolha == "5":
            print("Saindo do Sistema! Até Breve!")
            break
        else:
            print("Digite um número dentre as opções.")



def adicionar_tarefa(descricao):
    tarefas.append({"descricao": descricao, "concluida": False})
    print(f"Tarefa '{descricao}'  adicionada com sucesso!")

def visualizar_tarefas():
    if not tarefas:
        print("Nenhuma Tarefa foi encontrada!")
        return
    print("\nLista de Tarefas: ")
    for i, tarefa in enumerate(tarefas):
        status ="[X]" if tarefa["concluida"] else "[ ]"
        print(f"{i + 1}. {status} {tarefa["descricao"]}")

def marcar_tarefa(indice):
    if 0 <= indice <= len(tarefas):
        tarefas[indice] ["concluida"] = True
        print(f"Tarefa '{tarefas[indice]['descricao']} foi marcada como concluída! ' ")
    else:
        print("Índice de tarefa inválido")
        
def remover_tarefa(indice):
    if 0 <= indice <=len(tarefas):
        descricao = tarefas.pop(indice)["descricao"]
        print(f"Tarefa: {descricao} foi removida com sucesso!")
    else:
        print("Índice inválido.")

if __name__ == "__main__":
    main()