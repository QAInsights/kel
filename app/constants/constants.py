from app.__version__ import __version__

valid_ai_company_names = [
    "openai",
    "anthropic",
    "ollama"
]

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

valid_api_keys_env = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY"
}

emoji_info = ":speech_balloon:"
emoji_time = ":clock3:"
emoji_pencil = ":pencil:"
emoji_error = ":x:"
emoji_money = ":moneybag:"
emoji_thinking = ":thinking:"

app_name = "Kel"
app_version = __version__
app_description = """
Ask Kel. Your CLI based AI assistant.
Supported AI companies: OpenAI, Anthropic, and Ollama.
"""
epilog = 'Thank you for using Kel!'


exit_message = "Exiting chat mode... Bye!"

openai_response_prefix = ["Thinking...", "Crunching...", "Analyzing...",
                          "Processing...", "Calculating...", "Working...",
                          "Cooking", "Slicing...", "Dicing...", "Chopping..."]
openai_user_prefix = "Ask `Kel`: "
openai_assistant_prefix = "Assistant "

pricing_error_message = "Error: Pricing information is not available for this model."

