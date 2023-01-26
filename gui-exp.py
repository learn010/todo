import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add = sg.Button(key="add",bind_return_key=True, size=10, image_source="add.png",
                mouseover_colors="SlateGray",tooltip="Adds item to the todo list")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])

edit = sg.Button("edit", key="edit")
complete = sg.Button(key="complete",image_source="complete.png", mouseover_colors="SlateGray")
exit_button = sg.Button("exit")


window = sg.Window("test",
                   layout=[[clock],[label],
                           [input_box, add],
                           [list_box, edit, complete],
                           [exit_button]],
                   font=('helvetica',20))
while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime("%d %b, %Y, %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.insert(0,new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo+"\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.Popup("Please select an item to edit.",font=("helvetica", 20))
        case "complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item to Complete",font=("helvetica", 20))
        case "exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()