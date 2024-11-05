import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter To-Do")
input_box = sg.InputText(tooltip="Write To-Do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todolist",
                      enable_events=True, size=(43, 10))
edit_button = sg.Button("Edit")

window = sg.Window("To-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 10))
while True:
    event, values = window.read()
    match event:
        case sg.WINDOW_CLOSED:
            break
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todolist'].update(values=todos)
        case "Edit":
            edit_todo = values['todolist'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(edit_todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todolist'].update(values=todos)
        case 'todolist':
            window['todo'].update(value=values['todolist'][0])

window.close()
