import sys

from anthropic import AsyncAnthropic
from openai import AsyncOpenAI

from app.config import get_configs as config
from app.gpt.askanthropic import ask_anthropic
from app.gpt.askollama import ask_ollama
from app.gpt.askopenai import ask_openai
from app.inputs.gatekeeper import gatekeeper_tasks
from app.inputs.inputs import get_user_inputs_from_cli
from app.constants.constants import valid_ai_company_names
from app.utils.utils import print_in_color


class AICompany:
    def __init__(self, company_name):
        self.company_name = company_name


class GPTModel:
    def __init__(self, model_name, model_api_key, model_endpoint, model_prompt, model_max_token, model_temperature):
        super(AICompany).__init__()
        self.model_api_key = model_api_key
        self.model_name = model_name
        self.model_endpoint = model_endpoint
        self.model_max_token = model_max_token
        self.model_prompt = model_prompt
        self.model_temperature = model_temperature

        if config.get_default_company_name().lower() == "openai":
            self.client = AsyncOpenAI(api_key=self.model_api_key)
        elif config.get_default_company_name().lower() == "anthropic":
            self.client = AsyncAnthropic()

    @staticmethod
    def call_ollama(question=None, prompt=None, model=None, max_tokens=None):
        if model is None:
            model = config.get_ollama_default_model_name()
        if max_tokens is None:
            max_tokens = config.get_ollama_default_max_tokens()
        if prompt is None:
            prompt = config.get_ollama_default_prompt()

        ask_ollama(question=question, prompt=prompt, model=model, max_tokens=max_tokens)

    async def call_anthropic(self, question=None, prompt=None, model=None, max_tokens=None):
        if model is None:
            model = config.get_anthropic_default_model_name()
        if max_tokens is None:
            max_tokens = config.get_anthropic_default_max_tokens()
        if prompt is None:
            prompt = config.get_anthropic_default_prompt()

        await ask_anthropic(client=self.client, question=question, prompt=prompt, model=model, max_tokens=max_tokens)

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
        if model is None:
            model = config.get_openai_default_model()
        if temperature is None:
            temperature = config.get_openai_temperature()
        if max_tokens is None:
            max_tokens = config.get_openai_max_tokens()
        if prompt is None:
            prompt = config.get_openai_default_prompt()
        await ask_openai(client=self.client, question=question, prompt=prompt, model=model, temperature=temperature,
                         max_tokens=max_tokens)


async def gpt() -> None:
    """
    Main function
    Returns:

    """

    question, prompt, model, temperature, max_tokens, company = vars(get_user_inputs_from_cli()).values()
    company_name = gatekeeper_tasks(question, prompt, model, temperature, max_tokens, company)

    if company_name == "openai":
        openai = GPTModel(
            model_name=model,
            model_api_key=config.get_openai_key(),
            model_prompt=prompt,
            model_endpoint=f"{config.get_default_protocol()}://{config.get_default_openai_endpoint()}{config.get_default_openai_uri()}",
            model_max_token=max_tokens,
            model_temperature=temperature
        )

        await openai.ask_gpt(question, prompt, model, temperature, max_tokens)

    elif company_name == "anthropic":
        anthropic = GPTModel(
            model_name=model,
            model_prompt=prompt,
            model_max_token=max_tokens,
            model_api_key=None,
            model_endpoint=None,
            model_temperature=None
        )

        await anthropic.call_anthropic(
            question=question,
            prompt=anthropic.model_prompt,
            model=anthropic.model_name,
            max_tokens=anthropic.model_max_token
        )

    elif company_name == "ollama":
        ollama = GPTModel(
            model_name=model,
            model_prompt=prompt,
            model_endpoint=config.get_ollama_default_endpoint(),
            model_temperature=None,
            model_max_token=None,
            model_api_key=None
        )

        ollama.call_ollama(
            question=question,
            prompt=prompt,
            model=model,
            max_tokens=max_tokens
        )
