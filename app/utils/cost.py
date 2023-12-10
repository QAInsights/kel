import app.constants.base_price as base_price
from app.constants.constants import pricing_error_message


def calculate_cost(company, model, token):
    """
    Calculate cost
    :param company:
    :param model:
    :param token:
    :return:
    """

    if company == "openai":
        try:
            if model in base_price.openai_api_input_price_per_token:
                input_price = base_price.openai_api_input_price_per_token[model]
                output_price = base_price.openai_api_output_price_per_token[model]
                return (input_price + output_price) * int(token)
            else:
                raise KeyError(f"{pricing_error_message}")
        except Exception as e:
            print(f"Error: {e}")
            return 0
