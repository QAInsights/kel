import asyncio
import sys
import time

from openai import AsyncOpenAI
from anthropic import AsyncAnthropic

from app.config import get_configs as config
from app.constants.constants import *
from app.inputs.inputs import get_user_inputs_from_cli
from app.utils.utils import copy_to_clipboard, print_in_color, before_ask_gpt_display, after_ask_gpt_display
from app.gpt.askanthropic import ask_anthropic
from app.gpt.askollama import ask_ollama


class AICompany:
    def __init__(self, company_name):
        self.company_name = company_name


def call_ollama(question=None, prompt=None, model=None, max_tokens=None):
    if model is None:
        model = config.get_ollama_default_model_name()
    if max_tokens is None:
        max_tokens = config.get_ollama_default_max_tokens()
    if prompt is None:
        prompt = config.get_ollama_default_prompt()
    ask_ollama(question=question, prompt=prompt, model=model, max_tokens=max_tokens)


async def call_anthropic(client, question=None, prompt=None, model=None, max_tokens=None):
    if model is None:
        model = config.get_anthropic_default_model_name()
    if max_tokens is None:
        max_tokens = config.get_anthropic_default_max_tokens()
    if prompt is None:
        prompt = config.get_anthropic_default_prompt()

    await ask_anthropic(client=client, question=question, prompt=prompt, model=model, max_tokens=max_tokens)


class GPTModel:
    emoji_thinking = ":thinking_face:"

    def __init__(self, model_name, model_api_key, model_endpoint, model_prompt, model_max_token, model_temperature):
        super(AICompany).__init__()
        self.model_api_key = model_api_key
        self.model_name = model_name
        self.model_endpoint = model_endpoint
        self.model_max_token = model_max_token
        self.model_prompt = model_prompt
        self.model_temperature = model_temperature

        # create a client when the class is instantiated
        if config.get_default_company_name().lower() == "openai":
            self.client = AsyncOpenAI(api_key=self.model_api_key)
        elif config.get_default_company_name().lower() == "anthropic":
            self.client = AsyncAnthropic()

    async def ask_gpt(self, question=None, prompt=None, model=None, temperature=None, max_tokens=None, assistant=None,
                      file=None):
        """
        Ask GPT
        Args:
            question:

        Returns:
        :param file:
        :param prompt:
        :param max_tokens:
        :param temperature:
        :param model:
        :param question:

        """
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

            print_in_color(f"Thinking {GPTModel.emoji_thinking}.", config.get_info_color(), end="")

            if model in valid_openai_chat_models:
                start_time = time.time()
                print_in_color(".", config.get_info_color(), end="")

                response = await self.client.chat.completions.create(
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


async def gpt() -> None:
    """
    Main function
    Returns:

    """

    question, prompt, model, temperature, max_tokens = vars(get_user_inputs_from_cli()).values()
    if config.get_default_company_name() == "" or config.get_default_company_name() is None:
        print("Error: Company name is not set in the config file.")
        sys.exit(1)

    if config.get_default_company_name().lower() == "openai":
        openai = GPTModel(
            model_name=model,
            model_api_key=config.get_openai_key(),
            model_prompt=prompt,
            model_endpoint=f"{config.get_default_protocol()}://{config.get_default_openai_endpoint()}{config.get_default_openai_uri()}",
            model_max_token=max_tokens,
            model_temperature=temperature
        )

        await openai.ask_gpt(question, prompt, model, temperature, max_tokens)

    if config.get_default_company_name().lower() == "anthropic":
        anthropic = GPTModel(
            model_name=model,
            model_prompt=prompt,
            model_max_token=max_tokens,
            model_api_key=None,
            model_endpoint=None,
            model_temperature=None
        )

        await call_anthropic(
            client=anthropic.client,
            question=question,
            prompt=anthropic.model_prompt,
            model=anthropic.model_name,
            max_tokens=anthropic.model_max_token
        )

    if config.get_default_company_name().lower() == "ollama":
        ollama = GPTModel(
            model_name=model,
            model_prompt=prompt,
            model_endpoint=config.get_ollama_default_endpoint(),
            model_temperature=None,
            model_max_token=None,
            model_api_key=None
        )

        call_ollama(
            question=question,
            prompt=prompt,
            model=model,
            max_tokens=max_tokens
        )
