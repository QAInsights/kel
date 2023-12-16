import time

import google.generativeai as genai
from rich import box
from rich.console import Console
from rich.table import Table

from kel.config import get_configs as config
from kel.utils.utils import print_in_color, before_ask_gpt_display, after_ask_gpt_display, copy_to_clipboard


def ask_google(client=None, company=None, question=None, prompt=None, model=None, temperature=None):
    """
    Ask Google GPT

    :param client:
    :param question:
    :param prompt:
    :param model:
    :param temperature:
    :return:
    """
    model = genai.GenerativeModel(model)
    # Get safety settings
    safety_settings = []
    question = "Answer in " + config.get_response_language() + prompt + question
    before_ask_gpt_display(company=company, model=model.model_name)

    if config.get_google_safety_settings() is not None:
        for k, v in config.get_google_safety_settings().items():
            safety_settings.append({"category": k, "threshold": v})

    if config.get_default_google_streaming_response():
        start_time = time.time()
        response = model.generate_content(question,
                                          stream=True,
                                          safety_settings=safety_settings)
        response_time = time.time() - start_time
        for chunk in response:
            try:
                print_in_color(chunk.text, config.get_response_color())
            except Exception as e:
                print(f'{type(e).__name__}: {e}')
    else:
        start_time = time.time()
        response = model.generate_content(question,
                                          safety_settings=safety_settings)
        response_time = time.time() - start_time
        print_in_color(response.text, config.get_response_color())
        response = response.text
    if config.get_copy_to_clipboard():
        copy_to_clipboard(str(response.text))

    if config.get_google_prompt_feedback():
        table = Table(title="Prompt Feedback", show_header=True, header_style="bold blue", box=box.HEAVY)
        table.add_column("Category", style="cyan")
        table.add_column("Probability", style="green")
        for items in response.prompt_feedback.safety_ratings:
            table.add_row(str(items).split(":")[1].split("probability")[0], str(items).split(":")[-1])
        console = Console()
        console.print(table)

    if config.get_view_all_response_candidates():
        for count, response in enumerate(response.candidates):
            if count > 0:
                print_in_color(response.content.parts[0].text, config.get_response_color())

    after_ask_gpt_display(response_time=response_time)
    # Streaming response cannot be copied to clipboard
