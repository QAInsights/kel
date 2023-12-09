import os
import sys

from app.config import get_configs as config
from app.utils.utils import print_in_color
from app.constants.constants import valid_ai_company_names, valid_openai_chat_models, valid_anthropic_chat_models


def check_api_key(company_name=None):
    try:
        if company_name == "openai":
            if not os.getenv("OPENAI_API_KEY"):
                print_in_color("OPENAI_API_KEY is not set. Please set it in your environment variables.",
                               config.get_error_color())
                sys.exit(1)
        if company_name == "anthropic":
            if not os.getenv("ANTHROPIC_API_KEY"):
                print_in_color("ANTHROPIC_API_KEY is not set. Please set it in your environment variables.",
                               config.get_error_color())
                sys.exit(1)
    except Exception as e:
        print_in_color(f"Error: {e}", config.get_error_color())
        sys.exit(1)


def validate_chat_model(company_name=None, model_name=None):
    if company_name is not None:
        company_name = company_name.lower()
        if company_name == "openai":
            if model_name not in valid_openai_chat_models:
                print_in_color(f"Error: {model_name} is not a valid {company_name} chat model.",
                               config.get_error_color())
                print_in_color(f"Valid {company_name} chat models are: {valid_openai_chat_models}",
                               config.get_info_color())
                sys.exit(1)
        elif company_name == "anthropic":
            if model_name not in valid_anthropic_chat_models:
                print_in_color(f"Error: {model_name} is not a valid {company_name} chat model.",
                               config.get_error_color())
                print_in_color(f"Valid {company_name} chat models are: {valid_anthropic_chat_models}",
                                 config.get_info_color())
                sys.exit(1)
        else:
            pass


def gatekeeper_tasks(question=None, prompt=None, model=None, temperature=None, max_tokens=None, company=None, **kwargs):
    """
    Gatekeeper tasks
    :return:
    """
    if company is not None:
        company_name = company
    else:
        company_name = config.get_default_company_name().lower()

    if company_name == "" or company_name is None:
        print_in_color("Error: Company name is not set in the config file.", config.get_warning_color())
        sys.exit(1)

    if company_name.lower() not in valid_ai_company_names:
        print_in_color("Error: No valid AI company names found. Please check the config file.",
                       config.get_warning_color())
        sys.exit(1)

    if company_name.lower() == "openai" or company_name.lower() == "anthropic":
        check_api_key(company_name=company_name)

    if model is None:
        pass
    else:
        model = str(model).strip().lower()

    validate_chat_model(company_name=company_name, model_name=model)

    return company_name
