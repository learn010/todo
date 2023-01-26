import PySimpleGUI as sg

source = sg.FilesBrowse("source", key="source_file", size=10)
destination = sg.FolderBrowse("Destination",key="destination", size=10)
input_box_source = sg.InputText(key="source_path")
input_box_dest = sg.InputText(key="dest_path")
extract = sg.Button("extract", key="extract")
status = sg.Text("")

window = sg.Window("File Extractor", layout=[[],[input_box_source, source],
                                             [input_box_dest, destination],
                                             [extract, status]])

window.read()
window.close()
