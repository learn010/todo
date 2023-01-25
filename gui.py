import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add = sg.Button("add")


window = sg.Window("test",
                   layout=[[label], [input_box, add]],
                   font=('helvetica',20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()