import asyncio
from askgpt import main
from get_configs import get_enable_openai_assistant
from summon_assistant import summon_assistant

if __name__ == '__main__':
    print(get_enable_openai_assistant())
    if get_enable_openai_assistant():
        summon_assistant()
    else:
        asyncio.run(main())
