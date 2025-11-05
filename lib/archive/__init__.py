from lib.archive import *
from lib.interface import *

def archiveExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createArchive(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {name} criado com sucesso!')

def readArchive(name):
    try:
        a = open(name, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        header('Lista de tarefas cadastradas')
        for i in a:
            print(i)
             
    finally:
        a.close()  

def register(arc, task):
    try:
        a = open(arc, 'at')
    except:
        print('Ocorreu um erro na abertura do arquivo!') 
    else:
        try: 
            a.write(f'{task} \n')
        except:
            print('Ocorreu um erro ao cadastrar nova tarefa!') 
        else:
            print(f'Nova tarefa "{task}" agendada com sucesso!')
            a.close()      

def removeTask(arc, task):
    try:
        a = open(arc, 'rt')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        return
    except Exception:
        print('Ocorreu um erro ao abrir o arquivo!')
        return
    else:
        lines = a.readlines()
        a.close()

    task_stripped = task.strip()

    removed = False
    new_lines = []
    for line in lines:
        if line.strip() != task_stripped:
            new_lines.append(line)
        else:
            removed = True

    try:
        a = open(arc, 'wt')
        for line in new_lines:
            a.write(line)
        a.close()
    except Exception:
        print('Ocorreu um erro ao salvar o arquivo!')
        return

    if removed:
        print(f'Tarefa "{task}" removida com sucesso!')
    else:
        print(f'Tarefa "{task}" não encontrada.')