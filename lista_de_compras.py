listas = []

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Listar itens")
        print("3. Marcar item como comprado")
        print("4. Remover item")
        print("5. Editar quantidade de itens")
        print("6. Mostrar apenas itens não comprados")
        print("7.Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            descricao = input("Adicione seu item desejado: ")
            adicionar_item(descricao)
        elif escolha == "2":
            listar_item()
        elif escolha == "3":
            listar_item()
            try:    
                indice = int(input("Escolha o indice que deseja marcar: "))-1
                marcar_comprado(indice)
            except ValueError:
                print("Entrada inválida! Por favor digite um número existente")
        elif escolha == "4":
            listar_item()
            try:
                indice = int(input("Digite o índice do item que deseja remover: "))-1
                remover_item(indice)
            except ValueError:
                print("Entrada inválida! Por favor digite um número existente")
        elif escolha == "5":
            listar_item()
            try:
                indice = int(input("Digite o índice do item que deseja editar: "))-1
                editar_quantidade(indice)
            except ValueError:
                print("Entrada inválida! ")
        elif escolha == "6":
            listar_nao_comprado()
        elif escolha == "7":
            print("Saindo... Até Breve!")
            break
        else:
            print("Digite um indice existente! ")



def adicionar_item(descricao):
    try:
        quantidade = int(input("Adicione a quantidade: "))
    except ValueError:
        quantidade = 1
    listas.append({"descricao": descricao, "concluida": False})
    print(f"Item '{descricao}' adicionada com sucesso!")

def listar_item():
    if not listas:
        print("Nenhum item encontrado!")
        return
    print("\nLista de Itens: ")

    for i, lista in enumerate(listas):
        status = "[X]" if lista['concluida'] else "[]"
        print(f"{i+1}. {status} {lista['descricao']} (qtd: {lista['quantidade']})")

def marcar_comprado(indice):
    if 0 <= indice < len(listas):
        listas[indice] ["concluida"] = True
        print(f"Item '{listas[indice]['descricao']} foi marcada como concluída!")
    else:
        print("Índice de item inválido!")

def remover_item(indice):
    if 0<= indice < len(listas):
        descricao = listas.pop(indice)["descricao"]
        print(f"Item: '{descricao}' foi removido com sucesso!")
    else:
        print("Digite um índice válido")

def editar_quantidade(indice):
    if 0<= indice < len(listas):
        print(f"Quantidade atual: {listas[indice]['quantidade']}")
        try:
            nova_qtd = int(input("Nova quantidade: "))
            listas[indice]["quantidade"] = nova_qtd
            print("Quantidade atualizada com sucesso!")
        except ValueError:
            print("Digite um número válido!")
    else:
        print("Indice inválido! ")
def listar_nao_comprado():
    nao_comprados = [item for item in listas if not item['concluida']]
    if not nao_comprados:
        print("Todos os itens já foram comprados")
        return
    print("\nItens não comprados: ")
    for i, item in enumerate(listas):
        print(f"{i+1}. {item['descricao']} (qtd: {item['quantidade']})")


if __name__ == "__main__":
    main()