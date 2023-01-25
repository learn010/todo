import PySimpleGUI as sg
from zipcreator import make_archive


label1 = sg.Text("Select files to compress: ")
input1 = sg.Input(key='inputfiles')
choose1 = sg.FilesBrowse("Choose", key="files")
label2 = sg.Text("Select destination folder: ")
input2 = sg.Input(key='inputfolder')
choose2 = sg.FolderBrowse("Choose", key="folder")
output = sg.Text("",key="output")
compress_button = sg.Button("Compress")

window = sg.Window("File zipper",
                   layout=[[label1,input1,choose1],
                           [label2,input2,choose2],
                   [compress_button, output]])
while True:
    event, values = window.read()
    filepaths = values['files'].split(";")
    folderpath = values['folder']
    make_archive(filepaths,folderpath)
    window['output'].update(value="Compression complete.", text_color="green")



window.close()