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
        '-m',
        '--model',
        help='Model name: ',
        required=False
    )
    parser.add_argument(
        '-t',
        '--temperature',
        help='Temperature: ',
        required=False
    )
    parser.add_argument(
        '-mt',
        '--max_tokens',
        help='Max tokens: ',
        required=False
    )

    args = parser.parse_args()
    return args
