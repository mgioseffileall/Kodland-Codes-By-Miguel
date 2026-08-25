import random
import time

print('*' * 10, 'O jogo do Comerciante Misterioso', '*' * 10)

# Cartas do jogador

dragon = {}
dragon["Saúde"] = 10
dragon["Força"] = 8

ork = {}
ork["Saúde"] = 5
ork["Força"] = 4

elf = {}
elf["Saúde"] = 5
elf["Força"] = 4

goblins = {}
goblins["Saúde"] = 5
goblins["Força"] = 4

demonios = {}
demonios["Saúde"] = 10
demonios["Força"] = 8

cards_player = [dragon, elf, ork]
cards_comp = [elf, goblins, demonios]


print('Suas cartas:')
print('Dragão', dragon)
print('Elfo', elf)
print('Orc', ork)

while True:
    escolha = input('Escolha Dragão, Elfo ou Orc: ')

    if escolha == 'Dragão':
        card = dragon
        break
    elif escolha == 'Elfo':
        card = elf
        break
    elif escolha == 'Orc':
        card = ork
        break
    else:
        print('Carta inválida!')

time.sleep(1)

card_comp = random.choice(cards_comp)
print('Carta do inimigo:', card_comp)


turno = 1

while True:  
    print('--- TURNO', turno, '---')
    time.sleep(1)

    while True:  
        print('Você ataca!')
        time.sleep(1)

        card_comp['Saúde'] = card_comp['Saúde'] - card['Força']
        print('Vida do inimigo:', card_comp['Saúde'])

        if card_comp['Saúde'] <= 0:
            print('O inimigo foi derrotado!')
            break

        print('Turno do inimigo!')
        time.sleep(1)

        card['Saúde'] = card['Saúde'] - card_comp['Força']
        print('Sua vida:', card['Saúde'])

        if card['Saúde'] <= 0:
            print('Você perdeu!')
            break

        break 

    if card['Saúde'] <= 0 or card_comp['Saúde'] <= 0:
        break

    turno = turno + 1
