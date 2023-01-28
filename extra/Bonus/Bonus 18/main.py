import PySimpleGUI as sg
import extractor

source = sg.FileBrowse("source", key="source_file", size=10)
destination = sg.FolderBrowse("Destination",key="destination", size=10)
input_box_source = sg.InputText(key="source_path")
input_box_dest = sg.InputText(key="dest_path")
extract = sg.Button("extract", key="extract")
status = sg.Text("", key= "status")

window = sg.Window("File Extractor", layout=[[],[input_box_source, source],
                                             [input_box_dest, destination],
                                             [extract, status]])
while True:
    event, value = window.read()
    print(event,value)
    source_file = value['source_file']
    dest_loc = value['destination']
    extractor.extractor(source_file,dest_loc)
    window['status'].update(value="Extraction Complete", text_color="Green")

window.close()
