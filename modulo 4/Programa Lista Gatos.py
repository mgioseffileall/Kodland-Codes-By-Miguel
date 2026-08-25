import time

# Criar um programa para o Dragão e seus gatos 🐱
print('Programa da lista de gatos 🐱')
cats = {}
cats["Dracarian"] = "preto"
cats["Ragnarok"] = "branco"
cats["Peach"] = "laranja"
cats["Steve"] = "marrom"
cats["John"] = "cinza"

while True:
    opc_principais = input("Digite 1 para adicionar um gatinho a lista e 2 para exibir a lista")

    if opc_principais == "1":
        gato_adicionado = str(input("Digite o nome do gatinho:"))
        cor_gato = str(input("Digite a cor do gatinho:"))
        cats[gato_adicionado] = cor_gato
        print("Gatinho adicionado!")
        opc_secundarias = str(input("Digite 1 para voltar para o menu e 2 para sair."))
        if opc_secundarias == "1":
            print("voltando para o menu...")
            time.sleep(3)
            continue 

        elif opc_secundarias == "2":
            print("saindo do programa...")
            time.sleep(3)
            break 

       
        else:
            print("Comando errado!")
            continue

   
    elif opc_principais == "2":
        print(cats)
        opc_secundarias = str(input("Digite 1 para voltar para o menu e 2 para sair."))
        if opc_secundarias == "1":
            print("voltando para o menu...")
            time.sleep(3)
            continue 

        elif opc_secundarias == "2":
            print("saindo do programa...")
            time.sleep(3)
            break 

       
        else:
            print("Comando errado!")
            continue
        break
        
    else:
        print("Comando Inválido")
        continue
