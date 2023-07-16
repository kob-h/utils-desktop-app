from enum import Enum


class ApplicationElements(str, Enum):
    FILE_BROWSER_BUTTON = 'file_browser_button'
    FILE_BROWSER_INPUT_TEXT = 'file_browser_input_text'
    CONVERT_BUTTON = 'convert_button'
    RESULT_MULTILINE = 'result_multiline'
    COPY_TO_CLIPBOARD_BUTTON = 'copy_to_clipboard_button'
    COPIED_TO_CLIPBOARD_TEXT = 'copied_to_clipboard_text'
