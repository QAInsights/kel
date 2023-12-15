import os
import sys

from kel.config import get_configs as config
from kel.utils.utils import print_in_color
from kel.constants.constants import valid_ai_company_names, valid_openai_chat_models, valid_anthropic_chat_models, \
    valid_api_keys_env, valid_google_models


def check_api_key(company_name=None):
    try:
        for item in valid_api_keys_env:
            if company_name == item:
                if os.getenv(valid_api_keys_env[item]) is None:
                    print_in_color(
                        f"{valid_api_keys_env[item]} is not set. Please set it in your environment variables.",
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
        elif company_name == "google":
            if model_name not in valid_google_models:
                print_in_color(f"Error: {model_name} is not a valid {company_name} chat model.",
                               config.get_error_color())
                print_in_color(f"Valid {company_name} chat models are: {valid_google_models}",
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


def get_model_name(company_name):
    """
    Get model name
    :param company_name:
    :return:
    """
    if company_name is not None:
        company_name = company_name.lower()
        if company_name == "openai":
            return config.get_openai_default_model()
        elif company_name == "anthropic":
            return config.get_anthropic_default_model_name()
        elif company_name == "ollama":
            return config.get_ollama_default_model_name()
        elif company_name == "google":
            return config.get_default_google_model_name()
        else:
            print_in_color(f"Error in setting up the model. Please check the config file.", config.get_error_color())
            sys.exit(1)


def gatekeeper_tasks(question=None, prompt=None, model=None, temperature=None, max_tokens=None, company=None, **kwargs):
    """
    Gatekeeper tasks
    :return:
    """
    if company is None:
        company_name = config.get_default_company_name().lower()
    else:
        company_name = str(company).strip().lower()

    if company_name == "":
        print_in_color("Error: Company name is not set in the config file or not passed.", config.get_warning_color())
        sys.exit(1)

    if company_name.lower() not in valid_ai_company_names:
        print_in_color("Error: No valid AI company names found. Please check the config file.",
                       config.get_warning_color())
        sys.exit(1)

    if company_name.lower() == "openai" or company_name.lower() == "anthropic" or company_name.lower() == "google":
        check_api_key(company_name=company_name)

    if model is None:
        model = get_model_name(company_name=company_name)
    else:
        model = str(model).strip().lower()

    validate_chat_model(company_name=company_name, model_name=model)

    return company_name
