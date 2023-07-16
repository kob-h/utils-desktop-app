import PySimpleGUI
import base64
from src.constants.element_keys import ApplicationElements
from src.window_creator import create_app_window

window = create_app_window()


def get_base_64_encoded():
    path = values[ApplicationElements.FILE_BROWSER_INPUT_TEXT]
    with open(path, 'rb') as file:
        encoded = str(base64.b64encode(file.read()))[2:-1]

    return encoded


encoded_string = ''
while True:
    event, values = window.read()
    match event:
        case ApplicationElements.CONVERT_BUTTON:
            encoded_string = get_base_64_encoded()
            shortened = encoded_string[0:50]
            window[ApplicationElements.RESULT_MULTILINE].update(f"{shortened}...")
            window[ApplicationElements.COPIED_TO_CLIPBOARD_TEXT].update('')
        case ApplicationElements.COPY_TO_CLIPBOARD_BUTTON:
            if encoded_string:
                PySimpleGUI.clipboard_set(encoded_string)
                window[ApplicationElements.COPIED_TO_CLIPBOARD_TEXT].update('Copied to clipboard!')
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
