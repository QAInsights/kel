import time

from app.config import get_configs as config
from app.constants.constants import emoji_error, emoji_thinking, emoji_info, \
    valid_openai_chat_models
from app.utils.utils import copy_to_clipboard, print_in_color, before_ask_gpt_display, after_ask_gpt_display


async def ask_openai(client=None, question=None, prompt=None, model=None, temperature=None, max_tokens=None,
                     assistant=None,
                     file=None):
    try:

        if model is None:
            model = config.get_openai_default_model()
        if temperature is None:
            temperature = config.get_openai_temperature()
        if max_tokens is None:
            max_tokens = config.get_openai_max_tokens()
        if prompt is None:
            prompt = config.get_openai_default_prompt()

        before_ask_gpt_display(model=model)

        print_in_color(f"Thinking...🤔", config.get_info_color(), end="")

        if model in valid_openai_chat_models:
            start_time = time.time()
            print_in_color(".", config.get_info_color(), end="")

            response = await client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": f"{prompt}"},
                    {"role": "user",
                     "content": f"{question}. You will respond in {config.get_response_language()}"}
                ],
                max_tokens=int(max_tokens),
                temperature=float(temperature),
            )
            print_in_color(".", config.get_info_color())

            response_time = time.time() - start_time

            print_in_color(f"{emoji_info} {response.choices[0].message.content}", config.get_response_color())

            after_ask_gpt_display(response_time=response_time, end=" ")
            after_ask_gpt_display(consumed_tokens=response.usage.total_tokens, end=" ")

            if config.get_copy_to_clipboard():
                copy_to_clipboard(response.choices[0].message.content)

            return response.choices[0].message.content, response_time
        else:
            print_in_color(
                f"{emoji_error} Error: {model} is not a valid model name for {config.get_default_company_name()}.",
                config.get_warning_color())
            return f"Error: {model} is not a valid model name."

    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"
