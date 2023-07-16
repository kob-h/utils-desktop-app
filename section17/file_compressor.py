import PySimpleGUI
import os
import base64


select_files_label = PySimpleGUI.Text("Select files to compress")
selected_files_input_box = PySimpleGUI.InputText(tooltip="files to compress", key='selected_files')
choose_files_button = PySimpleGUI.Button("Choose")

select_destination_label = PySimpleGUI.Text("Select destination folder")
input_box = PySimpleGUI.InputText(tooltip="destination folder")
choose_destination_button = PySimpleGUI.Button("Choose")

convert_button = PySimpleGUI.Button("Convert")
copy_button = PySimpleGUI.Button("Copy to clipboard", key='clipboard_button')
qr_code = [PySimpleGUI.Image('QR.png', expand_x=True, expand_y=True)]

working_directory = os.getcwd()

status_text = PySimpleGUI.Text('', size=(20, 1), key="status")
window = PySimpleGUI.Window('File Zipper',
                            layout=[[select_files_label, selected_files_input_box, choose_files_button],
                                    [select_destination_label, input_box, choose_destination_button],
                                    [],
                                    [PySimpleGUI.FileBrowse(initial_folder=working_directory,
                                                            key="file_browser"),
                                     PySimpleGUI.InputText(key="blabla")],
                                     [convert_button],
                                    [PySimpleGUI.Multiline('some text', size=(20, 20), disabled=True, key='multiline'),
                                     copy_button],
                                    [status_text],
                                    [PySimpleGUI.Column([qr_code], justification='right')]],
                            font=('Helvetica', 20), margins=(0, 0))
while True:
    event, values = window.read()
    match event:
        case 'Convert':
            path = values['blabla']
            with open(path, 'rb') as file:
                encoded_string = str(base64.b64encode(file.read()))[2:-1]
                shortened = encoded_string[0:50]
                window['multiline'].update(f"{shortened}...")
                window['status'].update('')
        case 'clipboard_button':
            # copied_text = values['multiline']
            PySimpleGUI.clipboard_set(encoded_string)
            # PySimpleGUI.popup('Copied to clipboard!')
            window['status'].update('Copied to clipboard!')
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
