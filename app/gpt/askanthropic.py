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
    calc_token = ""
    stream = config.get_default_anthropic_streaming_response()
    print_in_color(f"Thinking..", config.get_info_color(), end="\n")

    start_time = time.time()
    response_time = time.time() - start_time

    if stream:
        response = await client.completions.create(
            model=model,
            max_tokens_to_sample=int(max_tokens),
            prompt=f"{HUMAN_PROMPT} {question}{AI_PROMPT}",
            stream=stream,
        )
        async for completion in response:
            print(f"{completion.completion}", end="", flush=True)
            calc_token += str(completion.completion)
        calc_token += question

    else:
        response = await client.completions.create(
            model=model,
            max_tokens_to_sample=int(max_tokens),
            prompt=f"{HUMAN_PROMPT} {question}{AI_PROMPT}",
            stream=stream,
        )
        calc_token = question + response.completion
        print_in_color(f"{response.completion}", config.get_response_color(), end="\n")
        # Streaming response cannot be copied to clipboard
        if config.get_copy_to_clipboard():
            copy_to_clipboard(response.completion)

    if config.get_display_response_time():
        print_in_color(f"\n{emoji_time} Response Time: {response_time:.2f} seconds",
                       config.get_info_color(), end=" ")

    if config.get_display_tokens():
        tokens_consumed = await client.count_tokens(calc_token)
        print_in_color(f"| {emoji_money} Total Consumed Tokens: {tokens_consumed}", config.get_info_color())

    # Chat mode
    # TO DO:
    # if config.get_anthropic_enable_chat():
    #     get_user_input = input("\n\nEnter your question: ")
    #     CHAT_AI_PROMPT = ["\n\nAssistant:"]
    #     CHAT_HUMAN_PROMPT = ["\n\nHuman:"]
    #     while True:
    #
    #         if get_user_input == "exit":
    #             break
    #         if get_user_input.strip():
    #
    #             print(f"Chat: {CHAT_HUMAN_PROMPT[-1]}")
    #             response = await client.completions.create(
    #                 model=model,
    #                 max_tokens_to_sample=int(max_tokens),
    #                 prompt=f"{CHAT_HUMAN_PROMPT[-1]} {get_user_input}{CHAT_AI_PROMPT[-1]}",
    #                 stream=stream,
    #             )
    #             CHAT_HUMAN_PROMPT.append(get_user_input)
    #             CHAT_AI_PROMPT.append(response.completion)
    #             print(f"Anthropic: {CHAT_AI_PROMPT[-1]}")
    #             get_user_input = input("\n\nEnter your question: ")
    #             continue
    #         else:
    #             get_user_input = input("\n\nEnter your question: ")
    #             continue
