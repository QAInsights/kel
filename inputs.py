import argparse


def get_user_inputs_from_cli():
    """
    Get user inputs
    Returns:

    """
    # Parse the arguments
    parser = argparse.ArgumentParser(
        prog='Kel',
        description='Ask Kel. Your CLI based AI assistant.',
        epilog='Thank you for using Kel!'
    )

    parser.add_argument(
        'question',
        help='Your question to Kel: ',
        type=str,
    )

    parser.add_argument(
        '-p',
        '--prompt',
        help='Prompt e.g "You are a web performance expert. You are helping a developer."',
        type=str,
        required=False
    )

    parser.add_argument(
        '-m',
        '--model',
        type=str,
        help='Model name e.g gpt-4',
        required=False
    )
    parser.add_argument(
        '-t',
        '--temperature',
        help='Temperature e.g 0.9',
        type=float,
        required=False
    )
    parser.add_argument(
        '-mt',
        '--max_tokens',
        type=int,
        help='Max tokens e.g 150',
        required=False
    )

    args = parser.parse_args()
    return args
