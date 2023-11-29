import pyperclip
from rich.console import Console


def copy_to_clipboard(text):
    """
    Copy to clipboard
    Args:
        text:

    Returns:

    """
    try:
        pyperclip.copy(text)
        # Copy the response to the clipboard and remove double quotes
        pyperclip.copy(text.strip().replace("\"", ""))
        print("Response copied to clipboard.")
    except Exception as e:
        print("Error copying to clipboard")
        print(e)


def print_in_color(text, color):
    """
    Print in color
    Args:
        text:
        color:

    Returns:
    :param color:
    :param text:

    """
    console = Console(log_time=False)

    console.log(text, style=color)
