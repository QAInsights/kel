from kel.__version__ import __version__

valid_ai_company_names = [
    "openai",
    "anthropic",
    "ollama",
    "google"
]

valid_ai_company_official_names = [
    "OpenAI",
    "Anthropic",
    "Ollama",
    "Google"
]

## MODELS START ##

valid_openai_chat_models = [
    "gpt-4",
    "gpt-4-32k",
    "gpt-4-1106-preview",
    "gpt-4-0613",
    "gpt-4-0314",
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-1106",
    "gpt-3.5-turbo-16k-0613",
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-0613"
]

valid_anthropic_chat_models = [
    "claude-2.1",
    "claude-instant-1.2",
    "claude-instant-1",
    "claude-2"
]

valid_google_models = [
    "models/gemini-pro"
]

## MODELS END ##

valid_api_keys_env = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY"
}

valid_show_options = [
    "companies",
    "general",
    "style",
    "stats",
    "all"
]


def get_official_names():
    if len(valid_ai_company_official_names) > 2:
        return ", ".join(valid_ai_company_official_names[:-1]) + ", and " + valid_ai_company_official_names[-1]
    if len(valid_ai_company_official_names) == 2:
        return valid_ai_company_official_names[0] + " and " + valid_ai_company_official_names[1]
    if len(valid_ai_company_official_names) == 1:
        return valid_ai_company_official_names[0]


# Emoji constants
emoji_info = ":speech_balloon:"
emoji_time = ":clock3:"
emoji_pencil = ":pencil:"
emoji_error = ":x:"
emoji_money = ":moneybag:"
emoji_thinking = ":thinking:"

# OpenAI constants
openai_response_prefix = ["Thinking...", "Crunching...", "Analyzing...",
                          "Processing...", "Calculating...", "Working...",
                          "Cooking", "Slicing...", "Dicing...", "Chopping..."]
openai_user_prefix = "Ask `Kel`: "
openai_assistant_prefix = "Assistant "
exit_message = "Exiting chat mode... Bye!"
pricing_error_message = "Error: Pricing information is not available for this model."

# App constants
app_name = "Kel"
app_version = __version__

app_description = f"""
Ask Kel. Your CLI based AI assistant.
Supported AI companies: {get_official_names()}.
"""
epilog = 'Thank you for using Kel!'
