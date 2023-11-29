import argparse
import sys
import pyperclip

from openai import OpenAI

import get_configs as config
from utils import copy_to_clipboard


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

        # create a client when the class is instantiated
        self.client = OpenAI(api_key=self.model_api_key)

    def ask_gpt(self, question=None, model=None, temperature=None, max_tokens=None):
        """
        Ask GPT
        Args:
            question:

        Returns:
        :param max_tokens:
        :param temperature:
        :param model:
        :param question:

        """
        try:
            if model is None:
                model = self.model_name
            if temperature is None:
                temperature = self.model_temperature
            if max_tokens is None:
                max_tokens = self.model_max_token

            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": f"{config.get_openai_default_prompt()}"},
                    {"role": "user", "content": f"{question}. You will respond in {config.get_response_language()}"}
                ],
                max_tokens=int(max_tokens),
                temperature=float(temperature),

            )
            print(response.choices[0].message.content)
            if config.get_copy_to_clipboard():
                copy_to_clipboard(response.choices[0].message.content)

            return response.choices[0].message.content

        except Exception as e:
            print(f"Error: {e}")
            return f"Error: {e}"


def get_user_inputs_from_cli():
    """
    Get user inputs
    Returns:

    """
    # Parse the arguments
    parser = argparse.ArgumentParser(
        prog='Kel',
        description='Ask Kel. Your CLI based AI assistant.',
        epilog='Thank you for using Kel!'
    )
    parser.add_argument(
        'question',
        help='Your question to Kel: ',
        type=str,
    )
    parser.add_argument(
        '-m',
        '--model',
        help='Model name: ',
        required=False
    )
    parser.add_argument(
        '-t',
        '--temperature',
        help='Temperature: ',
        required=False
    )
    parser.add_argument(
        '-mt',
        '--max_tokens',
        help='Max tokens: ',
        required=False
    )

    args = parser.parse_args()
    print(type(args))
    return args


def main():
    """
    Main function
    Returns:

    """
    question, model, temperature, max_tokens = vars(get_user_inputs_from_cli()).values()
    if config.get_default_company_name() == "" or config.get_default_company_name() is None:
        print("Error: Company name is not set in the config file.")
        sys.exit(1)

    if config.get_default_company_name() == "openai":
        openai = GPTModel(
            model_name=config.get_openai_default_model(),
            model_api_key=config.get_openai_key(),
            model_prompt=f"{config.get_openai_default_prompt()}.",
            model_endpoint=f"{config.get_default_protocol()}://{config.get_default_openai_endpoint()}{config.get_default_openai_uri()}",
            model_max_token=f"{config.get_openai_max_tokens()}",
            model_temperature=f"{config.get_openai_temperature()}"
        )
        print(question, model, temperature, max_tokens)
        openai.ask_gpt(question, model, temperature, max_tokens)

    if config.get_default_company_name() == "anthropic":
        print("Anthropic")
        # to do


if __name__ == '__main__':
    main()
