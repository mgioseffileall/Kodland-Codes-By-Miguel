
import time

while True:
    print('Digite 1 para criar uma escada e 2 para criar uma árvore:')
    escolha = int(input(" "))

    if escolha == 1:
        steps = int(input("Por favor, quantos degraus a escada terá: "))
        i = 1
        while i <= steps:
            print("*" * i)
            i += 1
            time.sleep(0.2)  

    elif escolha == 2:
        steps = int(input("Quantos níveis terá a árvore: "))
        i = 1
        while i <= steps:
            spaces = steps - i
            stars = 2 * i - 1
            print(" " * spaces + "*" * stars)
            i += 1

    else: 
        print("Esse comando não existe!")
        continue
