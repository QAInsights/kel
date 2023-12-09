import pyperclip
from rich.console import Console

from app.constants.constants import emoji_info, emoji_time, emoji_money
from app.config import get_configs as config


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
        print("Response copied to clipboard.", end="\n")
    except Exception as e:
        print("Error copying to clipboard")
        print(e)


def print_in_color(text, color, end="\n"):
    """
    Print in color
    Args:
        text:
        color:

    Returns:
    :param end:
    :param color:
    :param text:

    """
    console = Console(log_time=False)
    console.print(text, style=color, end=end)


def before_ask_gpt_display(*args, **kwargs):
    """
    Before ask gpt
    Returns:

    """
    end = "\n"
    if "end" in kwargs:
        end = kwargs.get("end")
    if "model" in kwargs:
        if config.get_display_llm_company_model_name():
            model = kwargs.get("model")
            print_in_color(f"{emoji_info} You are using {config.get_default_company_name()}'s Model: {model}",
                           config.get_info_color(), end=end)


def after_ask_gpt_display(*args, **kwargs):
    """
    After ask gpt
    Returns:

    """
    end = "\n"
    if "end" in kwargs:
        end = kwargs.get("end")
    if config.get_display_response_time():
        if "response_time" in kwargs:
            data = kwargs.get("response_time")
            if data:
                print_in_color(f"{emoji_time} Response Time: {data:.2f} seconds",
                               config.get_info_color(),
                               end=end)

    if config.get_display_tokens():
        if "consumed_tokens" in kwargs:
            data = kwargs.get("consumed_tokens")
            if data:
                print_in_color(f"{emoji_money} Total Consumed Tokens: {data}",
                               config.get_info_color(),
                               end=end)
