numero_procurado = int(input("Qual número você quer buscar entre 1 e 10? "))

tentativas = 0

for i in range(1, 11):
    tentativas += 1
    print("Analisando o número", i)
    
    if i == numero_procurado:
        print("Número", numero_procurado, "encontrado!")
        break

else:
    print("O número", numero_procurado, "não foi encontrado.")

print("Busca concluída após", tentativas, "tentativas.")
