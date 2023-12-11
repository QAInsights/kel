import time

from kel.config import get_configs as config
from kel.constants.constants import emoji_error, emoji_info, \
    valid_openai_chat_models
from kel.utils.cost import calculate_cost
from kel.utils.utils import copy_to_clipboard, print_in_color, before_ask_gpt_display, after_ask_gpt_display


async def ask_openai(client=None, question=None, prompt=None, model=None, temperature=None, max_tokens=None,
                     company=None, assistant=None, file=None):
    try:
        before_ask_gpt_display(company=company, model=model)

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

            after_ask_gpt_display(response_time=response_time,
                                  end=" ")
            after_ask_gpt_display(total_tokens=response.usage.total_tokens,
                                  end=" ")

            cost = calculate_cost(company,
                                  model,
                                  prompt_tokens=response.usage.prompt_tokens,
                                  completion_tokens=response.usage.completion_tokens
                                  )
            after_ask_gpt_display(cost=cost, end=" ")

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
