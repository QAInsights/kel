import kel.constants.base_price as base_price
from kel.constants.constants import pricing_error_message


def calculate_cost(company, model, prompt_tokens=0,
                   completion_tokens=0):
    """
    Calculate cost
    :param completion_tokens:
    :param prompt_tokens:
    :param company:
    :param model:
    :return:
    """

    if company == "openai":
        try:
            if model in base_price.openai_api_input_price_per_token:
                input_price = base_price.openai_api_input_price_per_token[model]
                output_price = base_price.openai_api_output_price_per_token[model]
                return (input_price * prompt_tokens) + (output_price * completion_tokens)
            else:
                raise KeyError(f"{pricing_error_message}")
        except Exception as e:
            print(f"Error: {e}")
            return 0
