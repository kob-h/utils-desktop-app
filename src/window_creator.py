from src.constants.element_keys import ApplicationElements
import os
import PySimpleGUI


def create_app_window():
    return PySimpleGUI.Window('Utils',
                              layout=create_layout(),
                              font=('Helvetica', 20), margins=(0, 0))


def create_layout():
    first_line = create_first_line()
    second_line = create_second_line()
    third_line = create_third_line()
    fourth_line = create_fourth_line()
    fifth_line = create_fifth_line()
    layout = [first_line, second_line, third_line, fourth_line, fifth_line]

    return layout


def create_first_line():
    working_directory = os.getcwd()
    file_browse = PySimpleGUI.FileBrowse(
        initial_folder=working_directory,
        key=ApplicationElements.FILE_BROWSER_BUTTON)
    browse_input = PySimpleGUI.InputText(key=ApplicationElements.FILE_BROWSER_INPUT_TEXT)

    return [file_browse, browse_input]


def create_second_line():
    convert_button = PySimpleGUI.Button('Convert', key=ApplicationElements.CONVERT_BUTTON)

    return [convert_button]


def create_third_line():
    multiline = PySimpleGUI.Multiline(size=(20, 20),
                                      disabled=True,
                                      key=ApplicationElements.RESULT_MULTILINE)
    copy_button = PySimpleGUI.Button("Copy to clipboard", key=ApplicationElements.COPY_TO_CLIPBOARD_BUTTON)

    return [multiline, copy_button]


def create_fourth_line():
    status_text = PySimpleGUI.Text('', size=(20, 1), key=ApplicationElements.COPIED_TO_CLIPBOARD_TEXT)

    return [status_text]


def create_fifth_line():
    qr_path = os.path.join('src', 'static', 'QR.png')
    qr_code = [PySimpleGUI.Image(qr_path, expand_x=True, expand_y=True)]
    column = PySimpleGUI.Column([qr_code], justification='right')

    return [column]
