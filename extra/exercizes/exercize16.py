import PySimpleGUI as sg

def convert(feet, inches):
    meters = feet * 0.3048 + inches *  0.0254
    return meters



ft_label = sg.Text("Enter feet: ")
inch_label = sg.Text("Enter inches: ")
input_ft = sg.InputText(key="feet")
input_inch = sg.InputText(key="inches")
conv_button = sg.Button("Convert")
result_label = sg.Text("",key="result_label")


window = sg.Window("convertor",
                   layout=[[ft_label,input_ft],
                           [inch_label, input_inch],
                           [conv_button,result_label]])

while True:
   event, values = window.read()
   print(f"event ={event} values = {values}")
   match event:
       case Convert:
           result = convert(float(values['feet']),float(values['inches']))
           window['result_label'].update(value=f"this is {result} meters")

window.close()