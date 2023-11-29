import os
import sys

import toml

config = toml.load("cli-config.toml")


def get_default_company_name():
    """
    Get the default company name
    Returns:

    """
    return config.get("general", {}).get("default_company_name", "openai")


def get_response_language():
    """
    Get the response language
    Returns:

    """
    return config.get("general", {}).get("default_language", "en")


def get_copy_to_clipboard():
    """
    Get the copy to clipboard
    Returns:

    """
    return config.get("general", {}).get("copy_to_clipboard", True)


def get_default_protocol():
    """
    Get the protocol
    Returns:

    """
    return config.get("general", {}).get("protocol", "https")


# OpenAI Configs
def get_openai_default_model():
    """
    Get the default model
    Returns:

    """
    return config.get("openai", {}).get("default_openai_model_name", "gpt-4")


def get_openai_default_prompt():
    """
    Get the default prompt
    Returns:

    """
    return config.get("openai", {}).get("default_openai_prompt",
                                        "You are an expert in software engineering. You are helping a developer.")


def get_default_openai_endpoint():
    """
    Get the default openai endpoint
    Returns:

    """
    return config.get("openai", {}).get("default_openai_endpoint", f"{get_default_protocol()}://api.openai.com")


def get_default_openai_uri():
    """
    Get the default openai uri
    Returns:

    """
    return config.get("openai", {}).get("default_openai_uri", "/v1/chat/completions")


def get_openai_model_name():
    """
    Get the openai model name
    Returns:

    """
    return config.get("openai", {}).get("default_model_name", "gpt-4")


def get_openai_key():
    """
    Get the openai key
    Returns:

    """
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        sys.exit("Error: OPENAI_API_KEY is not set in the environment variable.")
    return openai_key


def get_openai_max_tokens():
    """
    Get the openai max tokens
    Returns:

    """
    return config.get("openai", {}).get("default_openai_max_tokens", 150)


def get_openai_temperature():
    """
    Get the openai temperature
    Returns:

    """
    return config.get("openai", {}).get("default_openai_temperature", 0.9)


# Anthropic Configs
def get_anthropic_key():
    """
    Get the anthropic key
    Returns:

    """
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    if not anthropic_key:
        sys.exit("Error: ANTHROPIC_API_KEY is not set in the environment variable.")
    return anthropic_key


def get_anthropic_model_name():
    """
    Get the anthropic model name
    Returns:

    """
    return config.get("anthropic", {}).get("default_anthropic_model_name", "claude")


def get_anthropic_default_prompt():
    """
    Get the default prompt
    Returns:

    """
    return config.get("anthropic", {}).get("default_anthropic_prompt",
                                           "You are an expert in software engineering. You are helping a developer.")


def get_anthropic_default_endpoint():
    """
    Get the default anthropic endpoint
    Returns:

    """
    return config.get("anthropic", {}).get("default_anthropic_endpoint",
                                           f"{get_default_protocol()}://api.anthropic.com")


def get_anthropic_default_uri():
    """
    Get the default anthropic uri
    Returns:

    """
    return config.get("anthropic", {}).get("default_anthropic_uri", "/v1/chat/completions")


# Stats Configs
def get_display_cost():
    """
    Get the display cost
    Returns:

    """
    return config.get("stats", {}).get("display_cost", False)


def get_display_tokens():
    """
    Get the display tokens
    Returns:

    """
    return config.get("stats", {}).get("display_tokens", False)


def get_display_response_time():
    """
    Get the display response time
    Returns:

    """
    return config.get("stats", {}).get("display_response_time", False)


def get_response_color():
    """
    Get the response color
    Returns:

    """
    return config.get("style", {}).get("response_color", "green")


def get_warning_color():
    """
    Get the warning color
    Returns:

    """
    return config.get("style", {}).get("warning_color", "yellow")


def get_error_color():
    """
    Get the error color
    Returns:

    """
    return config.get("style", {}).get("error_color", "red")


def get_info_color():
    """
    Get the info color
    Returns:

    """
    return config.get("style", {}).get("info_color", "cyan")
