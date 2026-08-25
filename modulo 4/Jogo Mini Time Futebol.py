time = []
gols = {}
cartoes = {}

while True:
    print("1 - Criar time de mini-futebol")
    print("2 - Estatísticas de gols")
    print("3 - Controle de cartões vermelhos")
    print("4 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        time = []
        for i in range(5):
            jogador = input("Digite o nome do jogador: ")
            time.append(jogador)

        print("Time completo:")
        for jogador in time:
            print(jogador)

        remover = input("Deseja remover algum jogador? (sim ou não): ")

        if remover == "sim":
            nome = input("Digite o nome do jogador que deseja remover: ")
            if nome in time:
                time.remove(nome)

        print("Time atualizado:")
        for jogador in time:
            print(jogador)

    elif escolha == "2":
        gols = {}
        for i in range(3):
            nome = input("Digite o nome do jogador: ")
            quantidade = int(input("Digite o número de gols: "))
            gols[nome] = quantidade

        print("Estatísticas:")
        for nome in gols:
            print(nome, "-", gols[nome], "gols")

        atualizar = input("Digite o nome do jogador que deseja atualizar: ")

        if atualizar in gols:
            novo = int(input("Digite o novo número de gols: "))
            gols[atualizar] = novo

        print("Lista atualizada:")
        for nome in gols:
            print(nome, "-", gols[nome], "gols")

    elif escolha == "3":
        while True:
            print("1 - Adicionar jogador")
            print("2 - Alterar cartões")
            print("3 - Excluir jogador")
            print("4 - Mostrar lista")
            print("5 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Digite o nome do jogador: ")
                quantidade = int(input("Digite os cartões vermelhos: "))
                cartoes[nome] = quantidade

            elif opcao == "2":
                nome = input("Digite o nome do jogador: ")
                if nome in cartoes:
                    quantidade = int(input("Digite o novo número de cartões: "))
                    cartoes[nome] = quantidade

            elif opcao == "3":
                nome = input("Digite o nome do jogador: ")
                if nome in cartoes:
                    del cartoes[nome]

            elif opcao == "4":
                for nome in cartoes:
                    print(nome, "-", cartoes[nome], "cartões vermelhos")

            elif opcao == "5":
                break

    elif escolha == "4":
        break
