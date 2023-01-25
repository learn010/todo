import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo")
add = sg.Button("add")


window = sg.Window("test",layout=[[label], [input_box, add]])
window.read()
window.close()