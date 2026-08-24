import random

while True:
    escolha = input(
        "Escolha uma opção ou 'sair' para encerrar:\n"
        "1 - Programa de Asterisco de 5 linhas\n"
        "2 - Aplicativo de Moldura de Asteriscos\n"
        "3 - Soma de números de 1 até n\n"
        "4 - Jogo dos números\n"
        "Digite sua escolha: "
    )

    if escolha == 'sair':
        print("Encerrando o programa...")
        break

    elif escolha == '1':
        # Programa de Asterisco de 5 linhas
        for i in range(5):
            print("*" * (i + 1))

    elif escolha == '2':
        # Aplicativo de Moldura de Asteriscos
        nome = input("Digite seu nome: ")
        print("*" * (len(nome) + 4))
        print(f"* {nome} *")
        print("*" * (len(nome) + 4))

    elif escolha == '3':
        # Soma de números de 1 até n
        n = int(input("Digite um número: "))
        soma = 0
        for i in range(1, n + 1):
            soma += i
        print("A soma de todos os números de 1 até", n, "é:", soma)

    elif escolha == '4':
        # Jogo dos números
        numero_secreto = random.randint(1, 10)
        tentativas = 0

        while True:
            tentativa = int(input("Tente adivinhar o número (1-10): "))
            tentativas += 1

            if tentativa == numero_secreto:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break
            elif tentativas == 5:
                print(f"Você atingiu o número máximo de tentativas. O número secreto era {numero_secreto}.")
                break
            elif tentativa < numero_secreto:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")

    else:
        print("Opção inválida. Tente novamente.")

    print()  # linha em branco entre execuções
