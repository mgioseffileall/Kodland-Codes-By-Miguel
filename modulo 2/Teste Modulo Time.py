#Conecte o módulo time
import random
import time 

number = random.randint(1, 50)
print('E o vencedor é...')
time.sleep(2.5)
print('Participante número...')
time.sleep(2.5)
print(number)
print('Parabéns!')

print("\nHora atual:", time.ctime())
