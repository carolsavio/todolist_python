def line (size = 30):
    return '-' * size

def header(msg):
    size = 30
    print('-' * size)
    print(f'{msg.center(30)}')
    print('-' * size)

def menu(list):
    header('Lista de tarefas')
    c = 1
    for i in list:
        print(f'{c} - {i}')
        c += 1
    print(line())
    opc = int(input('Opção: '))
    return opc