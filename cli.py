from functions import get_todos, write_todos
import time

print(time.strftime("%b %d, %Y :: %H:%M:%S"))

while True:
    user_action = input("Enter choice__add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.title().strip('\n')
            print(f"{index+1}) {item}")

    elif user_action.startswith('edit'):
        try:
            n = int(user_action[5:])
            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[n-1] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Command is invalid..")
            continue

    elif user_action.startswith('complete'):
        try:
            n = int(user_action[9:])
            todos = get_todos()
            c = todos.pop(n-1).title().strip('\n')
            write_todos(todos)
            print(f"{c} - has been completed..")
        except IndexError:
            print("Index not found..")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command not recognized..")

print("Bye..")
