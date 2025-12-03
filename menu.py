tarefas = []

def menu():
    print("\n=== SISTEMA TO DO ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluida")
    print("4 - Editar tarefa")
    print("5 - Remover tarefa")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def adicionar(tarefas):
    titulo = input("Titulo da tarefa: ")
    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "estado": "pendente"
    }
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n=== SUAS TAREFAS ===")
    for t in tarefas:
        status = "concluída" if t["estado"] == "concluida" else "pendente"
        print(f"{t['id']} - {t['titulo']} [{status}]")

def concluir(tarefas):
    listar(tarefas)
    if not tarefas:
        return

    try:
        id_tarefa = int(input("Digite o ID da tarefa que deseja marcar como concluida: "))
    except ValueError:
        print("ID inválido.")
        return

    for t in tarefas:
        if t["id"] == id_tarefa:
            t["estado"] = "concluida"
            print("Tarefa marcada como concluida!")
            return

    print("Tarefa não encontrada.")

def editar(tarefas):
    listar(tarefas)
    if not tarefas:
        return

    try:
        id_tarefa = int(input("Digite o ID da tarefa para editar: "))
    except ValueError:
        print("ID inválido.")
        return

    for t in tarefas:
        if t["id"] == id_tarefa:
            novo_titulo = input("Digite o novo título da tarefa: ")
            t["titulo"] = novo_titulo
            print("Tarefa editada!")
            return

    print("Tarefa não encontrada.")

def remover(tarefas):
    listar(tarefas)
    if not tarefas:
        return

    try:
        id_tarefa = int(input("Digite o ID da tarefa que você quer remover: "))
    except ValueError:
        print("ID inválido.")
        return

    for t in tarefas:
        if t["id"] == id_tarefa:
            tarefas.remove(t)
            print("Tarefa removida com sucesso!")
            return

    print("Tarefa não encontrada.")

from menu import *

tarefas = []

while True:
    opcao = menu()

    if opcao == "1":
        adicionar(tarefas)
    elif opcao == "2":
        listar(tarefas)
    elif opcao == "3":
        concluir(tarefas)
    elif opcao == "4":
        editar(tarefas)
    elif opcao == "5":
        remover(tarefas)
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")
