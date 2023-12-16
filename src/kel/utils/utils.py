import sys

import pyperclip
from rich.console import Console
from rich.table import Table

from kel.constants.constants import emoji_info, emoji_time, emoji_money, valid_ai_company_official_names
from kel.config import get_configs as config
from kel.__version__ import __version__

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
        print("📝 Response copied to clipboard.", end="\n")
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
    if "company" in kwargs:
        company = kwargs.get("company")
    else:
        company = config.get_default_company_name()

    if "model" in kwargs:
        if config.get_display_llm_company_model_name():
            model = kwargs.get("model")
            print_in_color(f"{emoji_info} You are using {company}'s model: {model}",
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
                print_in_color(f"{emoji_time} Response Time: {data:.5f} seconds",
                               config.get_info_color(),
                               end=end)

    if config.get_display_tokens():
        if "total_tokens" in kwargs:
            data = kwargs.get("total_tokens")
            if data:
                print_in_color(f"{emoji_money} Total Tokens: {data}",
                               config.get_info_color(),
                               end=end)

    if config.get_display_cost():
        if "cost" in kwargs:
            data = kwargs.get("cost")
            if data:
                print_in_color(f"{emoji_money} Total Cost: {data:.6f} USD",
                               config.get_info_color(),
                               end=end)


def display_config(args=None):
    """
    Display config
    :param args:
    :return:
    """
    table = Table(title="Kel Config", show_header=True, header_style="bold blue")

    table.add_column("Name", style="cyan")
    table.add_column("Value", style="green")

    if args == "all":
        for key, value in config.get_all_config_keys_values().items():
            if type(key) is str:
                table.add_row(str(key), "")
                table.add_row("--" * 15, "--" * 15)

            if type(value) is dict:
                for k, v in value.items():
                    table.add_row(str(k), str(v))
                table.add_row("--" * 15, "--" * 15)
    else:
        for key, value in config.get_config_by_key(args).items():
            table.add_row(str(key), str(value))
    console = Console()
    console.print(table)

    sys.exit()


def cli_art():
    # Print the ascii art for the word `kel`
    print_in_color(rf"""
    |‾‾| /‾‾/   |‾‾‾‾‾‾|    |‾‾|   
    |  |/  /    |  (‾‾‾     |  |
    |     (     |   ‾‾‾|    |  |
    |  |\  \    |  (___     |  |___
    |__| \__\   |______|    |______|    v{__version__}
      """, config.get_info_color())
