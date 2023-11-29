import pyperclip


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
