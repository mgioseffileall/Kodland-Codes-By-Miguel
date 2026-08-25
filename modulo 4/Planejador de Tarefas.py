tasks = []
print('*' * 10, 'Planejador de Tarefas', '*' * 10)

while True:
    print('add, remove, mostrar, limpar, sair')
    comando = input()

    if comando == 'add':
        task = input()
        position = int(input())
        tasks.insert(position, task)

    elif comando == 'remove':
        position = int(input())
        tasks.pop(position)

    elif comando == 'mostrar':
        print(tasks)

    elif comando == 'limpar':
        tasks.pop()

    elif comando == 'sair':
        break
