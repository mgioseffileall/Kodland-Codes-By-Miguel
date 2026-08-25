import time 

while True:
    number = input("Digite um número de onde deseja começar a contagem regressiva: ")

    if number.isdigit():
        number = int(number)
        break
    else:
        print("Isso não é um número! Tente novamente.")

print("-" * 10)
while True:
    print(number)
    number -=1
    time.sleep(1)
    if number == 0:
        break

print("A contagem regressiva acabou!")
