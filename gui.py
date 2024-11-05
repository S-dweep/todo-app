import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter To-Do")
input_box = sg.InputText(tooltip="Write To-Do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 12))
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

window.close()
