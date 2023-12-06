import asyncio

from app.inputs.gatekeeper import gatekeeper_tasks

gatekeeper_tasks()

from app.gpt.askgpt import gpt
from app.config.get_configs import get_enable_openai_assistant
from app.assistant.summon_assistant import summon_assistant

if __name__ == '__main__':
    if get_enable_openai_assistant():
        summon_assistant()
    else:
        asyncio.run(gpt())
