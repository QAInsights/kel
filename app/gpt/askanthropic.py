import time

from anthropic import HUMAN_PROMPT, AI_PROMPT

from app.config import get_configs as config
from app.constants.constants import emoji_time, emoji_money
from app.utils.utils import copy_to_clipboard, print_in_color


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
    stream = (lambda x: config.get_default_anthropic_streaming_response())(None)

    start_time = time.time()
    response = await client.completions.create(
        model=model,
        max_tokens_to_sample=int(max_tokens),
        prompt=f"{HUMAN_PROMPT} {question}{AI_PROMPT}",
        stream=stream,
    )
    response_time = time.time() - start_time

    print_in_color(f"Thinking..", config.get_info_color(), end="\n")

    if stream:
        async for completion in response:
            print(f"{completion.completion}", end="", flush=True)
    else:
        print_in_color(f"{response.completion}", config.get_response_color(), end="\n")
        # Streaming response cannot be copied to clipboard
        if config.get_copy_to_clipboard():
            copy_to_clipboard(response.completion)

    if config.get_display_response_time():
        print_in_color(f"\n{emoji_time} Response Time: {response_time:.2f} seconds",
                       config.get_info_color(), end=" ")
