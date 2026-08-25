number_str = input("Por favor, insira um número: ")

sum_of_digits = 0

for digit in number_str:
    sum_of_digits += int(digit)

print("A soma dos dígitos no número que você forneceu: ", sum_of_digits)
