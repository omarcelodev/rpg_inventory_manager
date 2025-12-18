#Gerenciador de Inventário de RPG

#Biblioteca para permitir o salvamento do inventário e permitir comandos do sistema
import json
import os

#Itens do jogo
itens = {
    "armas": [
        "espada longa",
        "espada curta",
        "adaga",
        "machado de batalha",
        "machado leve",
        "lança",
        "arco curto",
        "arco longo",
        "besta",
        "cajado magico",
        "martelo de guerra",
        "maça pesada",
        "foice",
        "chicote",
        "bastão de combate"
    ],

    "armaduras": [
        "armadura leve",
        "armadura media",
        "armadura pesada",
        "armadura de couro",
        "armadura de ferro",
        "armadura de aço",
        "armadura encantada",
        "malha",
        "escudo pequeno",
        "escudo grande"
    ],

    "pocoes_consumiveis": [
        "poçao de cura",
        "poçao de mana",
        "poçao de stamina",
        "poçao de força",
        "poçao de velocidade",
        "poçao de invisibilidade",
        "poçao de resistencia a dano",
        "comida simples",
        "refeiçao completa",
        "agua",
        "elixir raro"
    ],

    "itens_magicos": [
        "amuleto magico",
        "anel magico",
        "pergaminho de magia",
        "grimorio",
        "pedra elemental",
        "orbe arcano",
        "runa encantada"
    ],

    "materiais": [
        "madeira",
        "pedra",
        "minerio de ferro",
        "minerio de prata",
        "minerio de ouro",
        "couro",
        "tecido",
        "ossos",
        "cristais",
        "polvora"
    ],

    "utilidades": [
        "corda",
        "tocha",
        "kit de primeiros socorros",
        "chave misteriosa",
        "mapa antigo",
        "moedas de bronze",
        "moedas de prata",
        "moedas de ouro",
        "ferramentas",
        "livro antigo",
        "reliquia desconhecida"
    ],

    "itens_raros": [
        "espada lendaria",
        "armadura divina",
        "coroa ancestral",
        "pedra filosofal",
        "amuleto do tempo",
        "escudo indestrutivel",
        "arco celestial"
    ]
}

#Inventário do jogo
inventario = []

#Função para definir o titulo permanente de "Abas"
def header(titulo):
    print(f"==={titulo}===\n")

#Limpa a tela do terminal
def clear():
    os.system('cls' if os.name == 'nt' else clear)

#Espera o usuário confirmar antes de limpar o terminal
def pause(msg = "Pressione ENTER para continuar..."):
    input(msg)

#Carrega inventário salvo em execuções passadas
def load__inventory():
    global inventario
    try:
        with open("inventario.json", "r", encoding="utf-8") as arquivo:
            inventario = json.load(arquivo)
    except FileNotFoundError:
        inventario = []
load__inventory()

#Adiciona a categoria do item automaticamente e verifica se o item está na lista de itens do jogo
def category_itens(name_item):
    for categoria, lista in itens.items():
        if name_item in lista:
            return categoria
                
    print("\nEsse item não existe no jogo.")
    input("Pressione ENTER para continuar...")
    return None

#Checa a quantidade do item que já existe no inventário
def check_qntd_atual(name_item):
    for item in inventario:
        if item["nome"].lower() == name_item:
            return item["quantidade"]
    return 0

#Captura a quantidade de itens que o usuário digitar para adicionar ao inventário
def qntd_itens(name_item):
    MAX = 50

    while True:
        clear()
        header("ADIÇÃO DE ITENS")

        print(f"Item selecionado: {name_item}")
        print(f"Tipo de item: {category_itens(name_item)}")

        qntd_item = int(input("Quantidade: +"))
        qntd_atual = check_qntd_atual(name_item)

        #Verifica se o inventário já está cheio
        if qntd_atual >= MAX:
            print(f"Inventário Cheio!\n")
            pause()
            return 0
        
        #Trata se a quantidade é válida
        if qntd_item < 1:
            print("Quantidade inválida!\n")
            pause()
            continue
        
        #Calcula o espaço livre no inventário
        free_space = MAX - qntd_atual

        #Caso a quantidade de item adicionado seja maio que o espaço livre o programa so adiciona quanto cabe
        if qntd_item > free_space:
            print(f"Só há espaço para {free_space} {name_item}.")
            print(f"+{free_space} {name_item} adicionad@(s) ao inventário.")
            pause()
            return free_space
        
        else:
            print(f"+{qntd_item} {name_item} adicionad@(s) no inventário.")
            pause()
        
        return qntd_item
    
#Adiciona Itens no inventário
def add_item():

    while True:
        clear()
        header("ADIÇÃO DE ITENS")

        name_item = input("Digite o nome do item que deseja adicionar: ").strip().lower()
        if category_itens(name_item) != None:
            break
    
    #Adiciona a quantidade de um item já existente no inventário
    for item in inventario:
        if item["nome"].lower() == name_item:
            print("\nEsse item já está no seu iventário.")
            pause()
            
            qntd_item = qntd_itens(name_item)
            item["quantidade"] += qntd_item

            return

    #Categoriza o item automaticamente. 
    type_item = category_itens(name_item)
    if type_item is None:
        return
        
    #Adiciona a quantidade de itens desejada
    qntd_item = qntd_itens(name_item)

    #Adiciona um novo item ao inventário
    new_item = {
        "nome": name_item, 
        "tipo": type_item, 
        "quantidade": qntd_item
    }

    inventario.append(new_item)

#Remove Itens do inventário    
def remove_item():
    while True:
        clear()
        header("REMOÇÃO DE ITENS")

        name_item = input("Digite o nome do item que deseja remover: ").strip().lower()

        for item in inventario:
            if item["nome"].lower() == name_item:
                while True:
                    clear()
                    header("REMOÇÃO DE ITENS")

                    print(f"Item selecionado: {name_item}")
                    print(f"Tipo de item: {category_itens(name_item)}")
                    qntd_itens = int(input("Quantidade: -"))

                    if qntd_itens < 1:
                        print("Quantidade Inválida!\n")
                        pause()
                    else:
                        break
                
                qntd_antiga = item["quantidade"]
                item["quantidade"] -= qntd_itens

                if item["quantidade"] <= 0:
                    inventario.remove(item)
                    print(f"Só existe {qntd_antiga} {name_item} no inventário")
                    print(f"-{qntd_antiga} removid@(s) do inventário")
                    print(f"{item['nome']} foi removido do inventário.\n")
                    pause()
                else:
                    print(f"-{qntd_itens} {name_item} removid@(s) do inventário")
                    print(f"{item['quantidade']} {item['nome']} restantes\n")
                    pause()

                return

        else:
            print("Esse item não existe no seu inventário!\n")
            pause()
            continue

#Imprime Lista de Itens do jogo
def print_category(itens, categoria):
    print(f"\n=== {categoria.upper()} ===")

    for i, item in enumerate(itens[categoria], start=1):
        print(f"{i:02d} - {item.capitalize()}")

#Consulta itens do jogo
def consult_item():
    while True:
        clear()
        header("CONSULTAR ITENS")

        type_item = input("Digite a categoria do item que deseja buscar: ").strip().lower()

        if type_item in itens:
            print_category(itens, type_item)
            pause()
            return
        else:
            print("Categoria não encontrada!\n")
            pause()

#Resumo do inventário com total de itens diferentes, total geral de unidades, lista dos tipos existentes
def resume_iventory():
    while True:
        clear()
        header("RESUMO INVENTÁRIO")

        if not inventario:
            print("Inventário vazio.\n")
            pause()
            return
        else:
            for item in inventario:
                print(f"Item: {item['nome']}")
                print(f"Tipo: {item['tipo']}")
                print(f"Quantidade: {item['quantidade']}")
                print("-" * 25)
            pause()
            return

#Salva o inventário
def save_inventory():
    with open("inventario.json", "w", encoding="utf-8") as arquivo:
        json.dump(inventario, arquivo, ensure_ascii=False, indent=4)

    clear()
    print("Inventário Salvo...\n")
    pause()

#Menu de Interação
def menu():
    while True:
        clear()
        print("=== INVENTARIO ===")
        print("(1) Adicionar Item")
        print("(2) Remover Item ")
        print("(3) Consultar Item")
        print("(4) Ver resumo do Inventário")
        print("(5) Salvar Inventário")
        print("(0) Sair do Inventário")
        opcao = int(input("Sua opção: "))

        if opcao == 1:
            clear()
            add_item()
        elif opcao == 2:
            clear()
            remove_item()
        elif opcao == 3:
            clear()
            consult_item()
        elif opcao == 4:
            clear()
            resume_iventory()
        elif opcao == 5:
            clear()
            save_inventory()
        elif opcao == 0:
            break
        else:
            print("Opção Inválidada! Tente Novamente.\n")
            input("Pressione ENTER para continuar...")

menu()