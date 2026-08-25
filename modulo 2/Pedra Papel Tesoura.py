import random
import time

player_score = 0
comp_score = 0
rodadas = 0

print('Bem vindo ao jogo de Pedra, Papel e Tesoura!')
time.sleep(2)
nome = input('Antes de começar, vou me apresentar. Sou a KodPlay e irei jogar contra você! Para nos conhecermos melhor, preciso saber seu nome: ')
print('Perfeito', nome + ',', 'agora podemos começar!')

# Jogar até completar 5 rodadas
while rodadas < 5:
    player = input(nome + ', Qual você quer escolher: Pedra, Papel ou Tesoura? ').lower()

    comp = random.randint(1, 3)

    if comp == 1:
        comp = "pedra"
    elif comp == 2:
        comp = "tesoura"
    elif comp == 3:
        comp = "papel"

    print("A KodPlay escolheu:", comp)
    print("O jogador escolheu:", player)

    # verifica quem venceu a rodada
    if (player == "pedra" and comp == "tesoura") or \
       (player == "tesoura" and comp == "papel") or \
       (player == "papel" and comp == "pedra"):
        print(nome, 'venceu a rodada!')
        player_score += 1

    elif player == comp:
        print("Empate na rodada! Ninguém ganha ponto.")

    else:
        print("KodPlay venceu a rodada!")
        comp_score += 1

    rodadas += 1
    print()  # linha em branco só pra separar visualmente

# Depois das 5 rodadas, verifica quem ganhou
print("Pontuação final após 5 rodadas:")
print(nome, ":", player_score)
print("KodPlay:", comp_score)

if player_score > comp_score:
    print(nome, "venceu a melhor de 5!")
elif comp_score > player_score:
    print("KodPlay venceu a melhor de 5!")
else:
    # Empate (por exemplo 2 x 2) -> rodada de desempate
    print("Empate! Vamos para a rodada de desempate!")

    while True:
        player = input("Desempate! Escolha Pedra, Papel ou Tesoura: ").lower()

        comp = random.randint(1, 3)
        if comp == 1:
            comp = "pedra"
        elif comp == 2:
            comp = "tesoura"
        elif comp == 3:
            comp = "papel"

        print("A KodPlay escolheu:", comp)
        print("O jogador escolheu:", player)

        if (player == "pedra" and comp == "tesoura") or \
           (player == "tesoura" and comp == "papel") or \
           (player == "papel" and comp == "pedra"):
            print(nome, "venceu o desempate!")
            break
        elif player == comp:
            print("Empate de novo no desempate! Vamos tentar mais uma vez.\n")
        else:
            print("KodPlay venceu o desempate!")
            break
