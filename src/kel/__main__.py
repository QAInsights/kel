import asyncio

from kel.inputs.gatekeeper import gatekeeper_tasks
from kel.gpt.askgpt import gpt
from kel.config.get_configs import get_enable_openai_assistant
from kel.assistant.summon_assistant import summon_assistant


def main():
    if get_enable_openai_assistant():
        summon_assistant()
    else:
        asyncio.run(gpt())


if __name__ == "__main__":
    main()
