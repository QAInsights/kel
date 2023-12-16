import argparse
import sys

from kel.config.get_configs import get_enable_openai_assistant

from kel.constants.constants import app_name, app_description, epilog, valid_show_options, valid_ai_company_names
from kel.utils.utils import display_config, cli_art


def get_user_inputs_from_cli():
    """
    Get user inputs
    Returns:

    """
    # Parse the arguments
    parser = argparse.ArgumentParser(
        prog=app_name,
        description=app_description,
        epilog=epilog,
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
        '-s',
        '--show',
        type=str,
        help='show default config e.g general, stats, style, companies',
        required=False
    )

    if '-s' not in sys.argv and '--show' not in sys.argv:
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

        parser.add_argument(
            '-v',
            '--version',
            action='version',
            version=''.format(version=cli_art()),
            help='show version'
        )

    args = parser.parse_args()

    if args.show in valid_show_options or args.show in valid_ai_company_names:
        display_config(args.show.lower())
    else:
        if args.show:
            print(f"Invalid show option: {args.show}. Valid options are: {valid_show_options}")
            sys.exit()

    return args
