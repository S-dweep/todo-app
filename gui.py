import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter To-Do")
input_box = sg.InputText(tooltip="Write To-Do")
add_button = sg.Button("Add")

window = sg.Window("To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()