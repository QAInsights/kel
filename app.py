import asyncio

from app.gpt.askgpt import main
from app.config.get_configs import get_enable_openai_assistant
from app.assistant.summon_assistant import summon_assistant

if __name__ == '__main__':
    if get_enable_openai_assistant():
        summon_assistant()
    else:
        asyncio.run(main())
