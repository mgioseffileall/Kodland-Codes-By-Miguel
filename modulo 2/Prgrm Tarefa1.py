import time 

print('Olá, bem-vindo ao app da escola de Hogwarts!')
print('-------------------------------------------------')
print("Login:")
print('-------------------------------------------------')

nome = input("Nome: ")
idade = int(input("Idade: "))
casa = input("Qual é sua casa?: ")
senha = input("Digite sua senha: ")

print('-------------------------------------------------')
print("Carregando...")
time.sleep(2)
print("Carregando...")
time.sleep(2)
print("Logado com sucesso!")
print('-------------------------------------------------')


if casa == "Grifinória":
    print("Casa Grifinória registrada!")

elif casa == "Sonserina":
    print("Casa Sonserina registrada!")

elif casa == "Corvinal":
    print("Casa Corvinal registrada!")

elif casa == "Lufa-Lufa":
    print("Casa Lufa-Lufa registrada!")

else:
    print("Casa não reconhecida, mas registrada mesmo assim.")


if idade > 7 and idade < 17:
    aluno = "Aluno"
    print("Perfeito, " + nome + "! Notamos que você é Aluno!")
else:
    aluno = "Graduado"
    print("Perfeito, " + nome + "! Notamos que você é Graduado!")

print('-------------------------------------------------')
print("Status final:")
print("Nome:", nome)
print("Idade:", idade)
print("Casa:", casa)
print("Categoria:", aluno)
