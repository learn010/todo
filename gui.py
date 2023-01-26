import functions
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add = sg.Button("add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])

edit = sg.Button("edit", key="edit")
complete = sg.Button("complete", key="complete")
exit_button = sg.Button("exit")


window = sg.Window("test",
                   layout=[[label],
                           [input_box, add],
                           [list_box, edit, complete],
                           [exit_button]],
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
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo+"\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(valuae=todos)
            window['todo'].update(value="")
        case "exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()