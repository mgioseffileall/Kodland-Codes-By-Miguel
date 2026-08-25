import random
import time
print('*' * 10, 'O jogo do Mercador Misterioso', '*' * 10)
# Cartas do jogador 
dragon {}
dragon["Saúde"] = 5 
dragon["Força"] = 5

elfo{}
elfo["Saúde"] = 7 
elfo["Força"] = 3

ork{}
ork["Saúde"] = 3
ork["Força"] = 3



#Jogo
cards = [dragon,elfo,orc]
print('Suas cartas:')
print('Dragão', dragon)
print('elfo', elfo)
print('Orc', orc)
card = input('É a sua vez! Qual carta você vai escolher?')
card_comp = random.choice(cards)
if card == 'Dragão':
    print('Sua carta é:', dragon)
    card = dragon
elif cards == 'elfo':
    print('Sua carta é:', elfo)
    card = elfo
elif card == 'Orc':
    print('Sua carta é:', orc)
    card = orc
time.sleep(1)
print('A vez do inimigo:', card_comp)
while True:
    print('Você ataca!')
    time.sleep(2)
    if card['Força'] >= card_comp['Saúde']:
        print('O inimigo foi derrotado!')
        break
    if card['Força'] < card_comp['Saúde']:
        print('O inimigo está ferido!')
        card_comp['Saúde'] = card_comp['Saúde'] - card['Força']
        print(card_comp)
        print('É a vez do inimigo!')
        time.sleep(2)
        if card_comp['Força'] >= carta['Saúde']:
            print('Você perdeu!')
            break
        elif card_comp['Força'] < carta['Saúde']:
            print('Você está ferido')
            card['Saúde'] = card['Saúde'] - card_comp['Força']
            print(card)
