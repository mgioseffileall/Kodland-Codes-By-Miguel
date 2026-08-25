import time
#introdução
print('Bem-vindo ao jogo da "regra dos 5 segundos"!')
time.sleep(1)
print('Aqui estão as regras:')
print('O programa fará uma pergunta e você tem 5 segundos para pensar em uma resposta')
time.sleep(2)

#pergunta 1
print('Pergunta 1')
time.sleep(1)
print('Quem era o personagem principal do desenho do Ursinho Pooh?')
time.sleep(2)
print('A: Ursinho Pooh')
print('B: Christopher Robin')

#laço
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

#resposta 1
q1 = input('Qual é a sua resposta? (A ou B)')
time.sleep(2)
if q1 == 'a':
    print('Correto! Parabéns')

else:
    print('Infelizmente, essa é uma resposta incorreta')
    print('A resposta correta é: A')

#######################################################################################

#pergunta 2
print('Pergunta 2')
time.sleep(1)
print('Qual é o nome do jogo onde um jogador mostra e os outros adivinham?')
time.sleep(2)
print('A: Uno')
print('B: Mímica')

#laço
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

#resposta 2
q1 = input('Qual é a sua resposta? (A ou B)')
time.sleep(2)
if q1 == 'b':
    print('Correto! Parabéns')

else:
    print('Infelizmente, essa é uma resposta incorreta')
    print('A resposta correta é: B')

#######################################################################################

#pergunta 3
print('Pergunta 3')
time.sleep(1)
print('Qual jogo tem um personagem principal chamado Steve?')
time.sleep(2)
print('A: Minecraft')
print('B: Roblox')

#laço
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

#resposta 3
q1 = input('Qual é a sua resposta? (A ou B)')
time.sleep(2)
if q1 == 'a':
    print('Correto! Parabéns')

else:
    print('Infelizmente, essa é uma resposta incorreta')
    print('A resposta correta é: A')

#######################################################################################

#pergunta 4
print('Pergunta 4')
time.sleep(1)
print('Qual é o nome do filme animado que apresenta o personagem Totoro?')
time.sleep(2)
print('A: Meu amigo Totoro')
print('B: Caramelo')

#laço
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

#resposta 4
q1 = input('Qual é a sua resposta? (A ou B)')
time.sleep(2)
if q1 == 'a':
    print('Correto! Parabéns')

else:
    print('Infelizmente, essa é uma resposta incorreta')
    print('A resposta correta é: A
