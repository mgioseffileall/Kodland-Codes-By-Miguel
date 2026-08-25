import random 

# cd = caractéres disponíveis
cd = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# cs = comprimento da senha 
cs = int(input("Digite o comprimento da senha: "))

senha = " "

for i in range(cs):
    senha += random.choice(cd)

print("Senha gerada: ", senha)
