import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Enter To-Do")
input_box = sg.InputText(tooltip="Write To-Do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todolist",
                      enable_events=True, size=(39, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button, exit_button],
                           [list_box, edit_button, complete_button]],
                   font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y :: %H:%M:%S"))
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
            try:
                edit_todo = values['todolist'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(edit_todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todolist'].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo first", font=('Helvetica', 10))
        case "Complete":
            try:
                complete_todo = values['todolist'][0]
                todos = functions.get_todos()
                todos.remove(complete_todo)
                functions.write_todos(todos)
                window['todolist'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select a todo first", font=('Helvetica', 10))
        case "Exit":
            break
        case 'todolist':
            window['todo'].update(value=values['todolist'][0])

window.close()
