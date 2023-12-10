import argparse

from app.config.get_configs import get_enable_openai_assistant

prog = 'Kel'
description = """
Ask Kel. Your CLI based AI assistant.
Supported AI companies: OpenAI, Anthropic, and Ollama.
"""
epilog = 'Thank you for using Kel!'


def get_user_inputs_from_cli():
    """
    Get user inputs
    Returns:

    """
    # Parse the arguments
    parser = argparse.ArgumentParser(
        prog=prog,
        description=description,
        epilog=epilog
    )

    if get_enable_openai_assistant():
        parser.add_argument(
            '-a',
            '--assistant',
            type=str,
            help='assistant name e.g PerfGPT',
            required=False
        )

        parser.add_argument(
            '-f',
            '--file',
            type=str,
            help='file path',
            required=False
        )

        return parser.parse_args()

    parser.add_argument(
        'question',
        help='your question to Kel: ',
        type=str,
    )

    parser.add_argument(
        '-p',
        '--prompt',
        help='prompt e.g "You are a web performance expert. You are helping a developer."',
        type=str,
        required=False
    )

    parser.add_argument(
        '-m',
        '--model',
        help='model name e.g gpt-4',
        type=str,
        required=False
    )
    parser.add_argument(
        '-t',
        '--temperature',
        help='temperature e.g 0.9',
        type=float,
        required=False
    )
    parser.add_argument(
        '-mt',
        '--max_tokens',
        type=int,
        help='max tokens e.g 150',
        required=False
    )
    parser.add_argument(
        '-c',
        '--company',
        type=str,
        help='company name e.g OpenAI',
        required=False
    )

    args = parser.parse_args()
    print("All arguments: ", args)
    return args

