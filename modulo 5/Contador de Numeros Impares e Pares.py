# Pedindo para o usuário inserir o número
number = input("Digite o número: ")

# Declarar contadores para os dígitos pares e ímpares
even_count = 0
odd_count = 0

# A tarefa: input retorna uma string; precisamos passar por cada caractere dessa string usando o loop for.
for digit in number:
    # Verificando se o dígito é par ou ímpar
    if int(digit) % 2 == 0:
        # Aumenta a contagem de dígitos pares aqui
        even_count +=1
    else:
        # Aumenta a contagem de dígitos ímpares aqui
        odd_count += 1
# Exibindo os resultados
print("Número de dígitos pares no número: ", even_count)
print("Número de dígitos ímpares no número: ", odd_count)
