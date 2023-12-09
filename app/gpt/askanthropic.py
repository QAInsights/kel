import time

from anthropic import HUMAN_PROMPT, AI_PROMPT

from app.config import get_configs as config
from app.constants.constants import emoji_time, emoji_money, emoji_info
from app.utils.utils import copy_to_clipboard, print_in_color, before_ask_gpt_display, after_ask_gpt_display


async def ask_anthropic(client, question, prompt, model, max_tokens):
    """
    Ask Anthropic GPT
    :param client:
    :param question:
    :param prompt:
    :param model:
    :param max_tokens:
    :return:
    """
    calc_token = ""
    stream = config.get_default_anthropic_streaming_response()

    before_ask_gpt_display(model=model)

    print_in_color(f"Thinking... 🤔", config.get_info_color(), end="\n")

    if stream:
        start_time = time.time()
        response = await client.completions.create(
            model=model,
            max_tokens_to_sample=int(max_tokens),
            prompt=f"{HUMAN_PROMPT} {question}{AI_PROMPT}",
            stream=stream,
        )
        response_time = time.time() - start_time
        async for completion in response:
            print(f"{completion.completion}", end="", flush=True)
            calc_token += str(completion.completion)
        calc_token += question

    else:
        start_time = time.time()
        response = await client.completions.create(
            model=model,
            max_tokens_to_sample=int(max_tokens),
            prompt=f"{HUMAN_PROMPT} {question}{AI_PROMPT}",
            stream=stream,
        )
        response_time = time.time() - start_time
        # Streaming response cannot be copied to clipboard
        if config.get_copy_to_clipboard():
            copy_to_clipboard(response.completion)

        calc_token = question + response.completion
        print_in_color(f"{response.completion}", config.get_response_color(), end="\n")

    calc_token = await client.count_tokens(calc_token)
    after_ask_gpt_display(response_time=response_time, end=" ")
    after_ask_gpt_display(consumed_tokens=calc_token, end=" ")
