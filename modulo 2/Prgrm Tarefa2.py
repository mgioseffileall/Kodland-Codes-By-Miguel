import time

print("Bem Vindo(a) ao nosso app de permissão de filmes!")
print('-------------------------------------------------')
nf = input("Qual é o nome do filme que você quer assistir?")
print('-------------------------------------------------')
print("Loading...")
time.sleep(3)
print("Parece que esse filme está registrado no nosso sistema!")
print('-------------------------------------------------')

idade = int(input("Quantos anos você tem?"))
print('-------------------------------------------------')
print("Loading...")
time.sleep(3)
print("Idade Registrada!")
print('-------------------------------------------------')


genero = str(input("Qual é o gênero do filme que  você quer assistir?"))
print('-------------------------------------------------')
print("Loading...")
time.sleep(3)
print("Loading...")
print('-------------------------------------------------')



if idade <= "12" or genero == "terror":
    print("Você não tem permissão para assistir esse filme!")

else:
    print("Permissão concedida!")
