import os
import sys
from kel.constants.constants import app_name
import toml

from kel.utils.utils import print_in_color


def get_config_file_location():
    """
    Get the config file location
    Returns:

    """
    config_file = os.getenv("KEL_CONFIG_FILE")
    try:
        if config_file and os.path.exists(os.path.expanduser(config_file)):
            return os.path.expanduser(config_file)
        elif os.path.exists(os.path.expanduser(f"~/.{app_name.lower()}/config.toml")):
            return os.path.expanduser(f"~/.{app_name.lower()}/config.toml")
        else:
            return os.path.expanduser("./config.toml")
    except Exception as e:
        print_in_color(f"Error: {e}", get_error_color())
        sys.exit(1)


try:
    config = toml.load(get_config_file_location())
except toml.TomlDecodeError as e:
    print(f"Invalid TOML file: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)


def get_all_config_keys_values():
    """
    Get all config keys values
    Returns:

    """
    all_config_keys_values = {}
    for k, v in config.items():
        all_config_keys_values.update({k: v})
    return all_config_keys_values


def get_config_by_key(key):
    """
    Get the config by key
    Args:
        key:

    Returns:

    """
    config = toml.load(get_config_file_location())
    return config[key]


def get_default_company_name():
    """
    Get the default company name
    Returns:

    """
    return config.get("general", {}).get("default_company_name", "openai")


def get_display_llm_company_model_name():
    """
    Get the display llm company model name
    Returns:

    """
    return config.get("general", {}).get("display_llm_company_model_name", False)


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


def get_enable_openai_assistant():
    """
    Get the enable openai assistant
    Returns:

    """
    return config.get("openai_assistant", {}).get("enable_openai_assistant", False)


def get_openai_assistant_model_name():
    """
    Get the openai assistant model name
    Returns:

    """
    return config.get("openai_assistant", {}).get("openai_assistant_model_name", "gpt-4-1106-preview")


def get_openai_assistant_instructions():
    """
    Get the openai assistant instructions
    Returns:

    """
    return config.get("openai_assistant", {}).get("openai_assistant_instructions",
                                                  "Analyse the file and answer questions about performance stats")


def get_openai_assistant_prompt():
    """
    Get the openai assistant prompt
    Returns:

    """
    return config.get("openai_assistant", {}).get("openai_assistant_prompt",
                                                  """
                                        Everything should be in a table format so that I can understand it.
                                        Do not give detailed explanation. If you find any bottleneck, please share that as well.
                                        """
                                                  )


def get_openai_assistant_choices():
    """
    Get the openai assistant choices
    :return:
    """
    try:
        openai_assistant_choices = [
            config.get("openai_assistant", {}).get(f"openai_assistant_choice_{choice}")
            for choice in range(1, 5)
            if config.get("openai_assistant", {}).get(f"openai_assistant_choice_{choice}") is not None
        ]

        if len(openai_assistant_choices) != 4:
            sys.exit(f"""
    OpenAI Assistant choices are not properly set in the config file. It must have four choices.
    Please check the config file at {get_config_file_location()}.
                """)

        return openai_assistant_choices

    except Exception as e:
        print(f"""
    OpenAI Assistant choices are not properly set in the config file. It must have four choices.
    Please check the config file at {get_config_file_location()}.
    Error: {e}
            """)
        sys.exit(f"Error: {e}")


def get_openai_delete_assistant_at_exit():
    """
    Get the openai delete assistant at exit
    Returns:

    """
    return config.get("openai_assistant", {}).get("delete_openai_assistant_at_exit", True)


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


def get_anthropic_default_model_name():
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


def get_anthropic_default_max_tokens():
    """
    Get the default max tokens
    Returns:

    """
    return config.get("anthropic", {}).get("default_anthropic_max_tokens", 100)


def get_default_anthropic_streaming_response():
    """
    Get the default streaming response settings
    Returns:

    """
    return config.get("anthropic", {}).get("default_anthropic_streaming_response", False)


def get_anthropic_enable_chat():
    """
    Get the enable chat
    Returns:

    """
    return config.get("anthropic", {}).get("anthropic_enable_chat", False)


def get_ollama_enable_chat():
    """
    Get the enable chat
    Returns:

    """
    return config.get("ollama", {}).get("ollama_enable_chat", False)


def get_ollama_default_model_name():
    """
    Get the default model name
    Returns:

    """
    return config.get("ollama", {}).get("default_ollama_model_name", "ollama2")


def get_ollama_default_prompt():
    """
    Get the default prompt
    Returns:

    """
    return config.get("ollama", {}).get("default_ollama_prompt",
                                        "You are an expert in software engineering. You are helping a developer.")


def get_ollama_default_max_tokens():
    """
    Get the default max tokens
    Returns:

    """
    return config.get("ollama", {}).get("default_ollama_max_tokens", 100)


def get_ollama_streaming_response():
    """
    Get the streaming response
    Returns:

    """
    return config.get("ollama", {}).get("default_ollama_streaming_response", False)


def get_ollama_default_endpoint():
    """
    Get the endpoint
    Returns:

    """
    return config.get("ollama", {}).get("default_ollama_endpoint", f"{get_default_protocol()}://api.ollama.ai")


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


def get_default_google_model_name():
    """
    Get the default google model name
    Returns:

    """
    return config.get("google", {}).get("default_google_model_name", "gemini-pro")


def get_default_google_streaming_response():
    """
    Get the default google streaming response
    Returns:

    """
    return config.get("google", {}).get("default_google_streaming_response", False)


def get_default_google_prompt():
    """
    Get the default google prompt
    Returns:

    """
    return config.get("google", {}).get("default_google_prompt",
                                        "You are an expert in software engineering. You are helping a developer.")


def get_google_key():
    """
    Get the openai key
    Returns:

    """
    google_key = os.getenv("GOOGLE_API_KEY")
    if not google_key:
        sys.exit("Error: GOOGLE_API_KEY is not set in the environment variable.")
    return google_key


def get_google_prompt_feedback():
    """
    Get the prompt feedback
    Returns:

    """
    return config.get("google", {}).get("enable_prompt_feedback", False)


def get_view_all_response_candidates():
    """
    Get the view all response candidates
    Returns:

    """
    return config.get("google", {}).get("view_all_response_candidates", False)


def get_google_safety_settings():
    """
    Get the Google safety settings
    Returns:

    """
    return config.get("google", {}).get("safety_settings", None)
