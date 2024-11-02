FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as ff:
        r_todos = ff.readlines()
    return r_todos


def write_todos(w_todos, filepath=FILEPATH):
    with open(filepath, 'w') as ff:
        ff.writelines(w_todos)
