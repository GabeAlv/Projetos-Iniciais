'''
Projeto ToDoList 1.0
'''
import json

def salvar_arquivo(): # Salva a lista de tarefas em um arquivo json
    with open('Lista_de_tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def abrir_arquivo(): # abre o arquivo json
    try: # Se tiver o arquivo vai retornar os valores de dentro do arquivo
        with open('Lista_de_tarefas.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError: # caso não tenha o arquivo, vai retornar uma lista vazia
        return []
def menu_principal(): # função que pega as escolhas do usuário e mostra o menu
    if not tarefas:
        tarefa = input('Adicione uma tarefa primeiro: ')
        tarefas.append({"nome": tarefa, "concluida": False})

    mostrar_tarefas()

    try:
        escolha = int(input(f'''\nOlá, você está no menu da lista de tarefas, o que gostaria de fazer?:
Digite 0 - (Para salvar e sair)
Digite 1 - (Adicionar uma tarefa)
Digite 2 - (Remover uma tarefa)
Digite 3 - (Marcar uma tarefa como concluída)
Opção: '''))
    except ValueError:
        print('DIGITE UM NÚMERO')
        return -1
    return escolha

def mostrar_tarefas(): # função para mostrar as tarefas feitas e não feitas
    print('Sua lista de tarefas:')
    if not tarefas:
        print('Nenhuma Tarefa atualmente')
    for t in tarefas:
        if t["concluida"] == False:
            print(f'{t["nome"]}⏳')
        else:
            print(f'{t["nome"]}✅')

def adicionar_tarefas(): # função para adicionar itens a lista de tarefas
    tarefa = input('Adicione uma tarefa: ')
    for t in tarefas:
        if t['nome'] == tarefa:
            print('Há uma tarefa igual a esta')
            return tarefas
    tarefas.append({"nome": tarefa, "concluida": False})
    return tarefas

def remover_tarefas(): # função para remover itens da lista de tarefas
    mostrar_tarefas()
    tarefa = input(f'Qual tarefa você pretende remover?: ')
    for t in tarefas:
        if t['nome'] == tarefa:
            tarefas.remove(t)
            return tarefas

def marcar_concluida(): # função para marcar as tarefas como concluida
    mostrar_tarefas()
    tarefa = input(f'Qual tarefa você pretende marcar como concluída?: ')
    for t in tarefas:
        if t['nome'] == tarefa and t['concluida'] == False:
            t['concluida'] = True
    return tarefas

def funcao_principal(): # função principal que executa todos os outros blocos
    while True: # looping para deixar o programa funcionando
        escolha = menu_principal()
        if escolha == 0: # sai do programa
            salvar_arquivo() # salva o arquivo ao sair do programa
            break
        elif escolha == 1: # adiciona um item a lista
            adicionar_tarefas()
        elif escolha == 2: # remove uma tarefa
            remover_tarefas()
        elif escolha == 3: # marca uma tarefa como concluida
            marcar_concluida()
        elif escolha == -1: # reinicia o programa caso a escolha não seja um número
            continue

tarefas = abrir_arquivo() # abre o arquivo json, e caso não tenha o arquivo json ele será uma lista vazia

funcao_principal() # chamando a função principal
