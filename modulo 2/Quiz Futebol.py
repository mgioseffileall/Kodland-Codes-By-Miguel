point = 0

#Escreva o seu próprio quiz!
nome = input("Olá! Qual é seu nome?")
print("Bem vindo" + " " + nome + "!" + " " + "está preparado para testar seus conhecimentos sobre futebol?")

print("----------------------------------------------------------------")
print("Primeira pergunta!")

p1 = input("Qual seleção venceu a Copa do Mundo de 2002?")

if p1 == "Brasil":
  print("Resposta correta!")
  point += 1
  print('Sua pontuação:', point)

else:
  print("Você errou!")

print("----------------------------------------------------------------")
print("Segunda pergunta!")

p2 = input("Quem é conhecido como O Rei do Futebol?")

if  p2 == "Pelé":
    print("Resposta correta!")
    point +=1
    print('sua pontuação:', point)

else:
    print("Resposta errada!")


print("----------------------------------------------------------------")
print("terceira pergunta!")

p3 = input("Em que clube Lionel Messi começou a carreira profissional?")

if p3 == "Barcelona":
    print("Resposta correta!")
    point += 1
    print('sua pontuação:', point)

else:
    print("Não foi dessa vez, você errou!")

print("----------------------------------------------------------------")
print("quarta pergunta!")

p4 = input("Qual jogador foi campeão da liga italiana: Ibraimovich ou Maradona")

if p4 == "Maradona" or "Ibaimovich":
    print("Sua resposta está correta!")
    point += 1
    print("sua pontuação:", point)

else:
    print("Sua resposta está errada!")

print("----------------------------------------------------------------")
print("quinta e última pergunta!")

print('Para poder pomtuar nessa questão, responda duas perguntas corretamente!')

p5 = input("Qual foi o primeiro time que ganhou uma copa do mundo")
p6 = input("Quantas Libertadores o Vasco ganhou?")

if p5 == "Uruguai" and p6 == "1":
    print("Exato! Você está certo!")
    point += 1
    print("Sua pontuação:", point)

else:
    print("Não foi dessa vez!")




print("----------------------------------------------------------------")
print("Parabéns! Sua pontuação final:", point)
