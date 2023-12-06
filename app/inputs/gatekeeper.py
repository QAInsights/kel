import os
import sys

from app.config.get_configs import config, get_error_color, get_default_company_name
from app.utils.utils import print_in_color


def check_openai_key():
    try:
        if not os.getenv("OPENAI_API_KEY"):
            print_in_color("OPENAI_API_KEY is not set. Please set it in your environment variables.",
                           get_error_color())
            sys.exit(1)
    except Exception as e:
        print_in_color(f"Error: {e}", get_error_color())
        sys.exit(1)


def gatekeeper_tasks():
    """
    Gatekeeper tasks
    :return:
    """

    company_name = get_default_company_name()
    if company_name == "openai":
        check_openai_key()
