import PySimpleGUI as sg

ft_label = sg.Text("Enter feet: ")
inch_label = sg.Text("Enter inches: ")
input_ft = sg.InputText()
input_inch = sg.InputText()
conv_button = sg.Button("Convert")

window = sg.Window("convertor",
                   layout=[[ft_label,input_ft],
                           [inch_label, input_inch],
                           [conv_button]])

window.read()
window.close()