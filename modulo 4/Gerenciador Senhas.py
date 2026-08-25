import random
import time

senha = {}
senha['João'] = '123-1445'
senha['Ana'] = '145-1789'
senha['Marcelo'] = '322-3456'

def menu():
    print("Bem Vindo ao menu!")
    print("Aqui você pode selecionar a opção que você quiser!")
    print("1 - Adicionar chave")
    print("2 - Editar chave")
    print("3 - Remover chave")
    print("4 - Visualizar lista")
    print("5 - Aleatorizar")
    print("6 - Sair")
    #Uma nova opção apenas para essa apresentação.
    print("7 - Apresentação do projeto.")
   

while True:
    menu()
    escolha = input(" ")

    if escolha == "1":
        key = input('Qual chave você gostaria de adicionar?')
        name = input('Qual nome essa chave deverá ter?')
        senha[key] = name
        print(senha)
        
    
    elif escolha == "2":
        print(senha)
        nome = input("Qual nome você quer editar?")
        if nome in senha:
            print("Nome encontrado!")
            print("1 - Alterar nome")
            print("2 - Alterar senha")
            tipo = input("Escolha: ")

            if tipo == "1":
                novo_nome = input("Digite o novo nome: ")
                senha[novo_nome] = senha.pop(nome)
                print("Novo nome adicionado!")




            elif tipo == "2":
                nova_senha = input("Digite a nova senha: ")
                senha[nome] = nova_senha
                print("Senha alterada!")


        else:
            print("Nome não encontrado!")

    elif escolha == "3":
        print(senha)
        nome = input("Qual chave você quer remover? ")
        if nome in senha:
            del senha[nome]
            print("Chave removida com sucesso!")
        
        else:
            print("Nome não encontrado!")

    elif escolha == "4":
        print(senha)

    elif escolha == "5":
        senha_aleatoria = random.randint(100, 100000000)
        key = input('Qual o nome da chave?')
        senha[key] = random
        print(senha)

    elif escolha == "6":
        break 

    elif escolha == "7":
        print("Bem vindos à apresentação do meu projeto!")
        time.sleep(2)
        print("Vamos começar!")
        time.sleep(1)
        print("Respondendo pergunta 1: Eu esscolhi o projeto de gerador de senhas porque achei uma proposta interessante e achei que seria bem legal de fazer!")
        time.sleep(5)
        print("Respondendo pergunta 2: Eu consegui terminar meu projeto a tempo, faltou apenas alguns ajustes, mas eu resolvi isso durante a aula enquanto testava o programa.")
        time.sleep(5)
        print("Respondendo pergunta 3: No meu ponto de vista, o programa ficou bem completo, que na minha percepção não precisa de nenhum ajuste.")
        time.sleep(5)
        print("Respondendo pergunta 4: Eu passei bastante dificuldade na questão da segunda opção do meu programa, a opção de editar chaves. Eu passei um pouco de dificuldade pois tive que pesquisar como os comandos funcionavam porque ainda não estudei isso.")
        time.sleep(5)
        print("Respondendo pergunta 5: O projeto inteiro foi muito legal e divertido de fazer, mesmo que eu tenha passado por algumas dificuldades, isso não transformou o projeto numa coisa chata. Eu gosto muito quando temos que fazer esses projetos individuais pois colocamos em prática o que aprendemos durante as aulas.")
        time.sleep(1)
        print("Muito obrigado!")
        break
    
    else:
        print("Esse comando não existe!")
        continue
