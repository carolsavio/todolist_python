from lib.archive import *
from lib.interface import *

arc = 'todolist.txt'

if not archiveExist(arc):
    createArchive(arc)

header('To-Do List')

while True:
    ans = menu(['Ver tarefas agendadas', 'Cadastrar nova tarefa', 'Concluir tarefa', 'Sair'])
    if ans == 1:
    #opção de criar nova tarefa na lista
        readArchive(arc)
    elif ans == 2:
        header('Cadastrar tarefa')
        task = str(input('Nova tarefa: '))
        register(arc, task)
    elif ans == 3:
        task = str(input('Nome da tarefa a ser removida: '))
        removeTask(arc, task)
    elif ans == 4:
        header('Saindo...')
        break
    else:
        print('Opção inválida!')