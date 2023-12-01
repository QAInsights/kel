import os
import time

from openai import OpenAI

from get_configs import get_openai_assistant_model_name, get_openai_assistant_instructions, get_openai_assistant_prompt

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Assistant:
    def __init__(self, assistant_name, file):
        self.assistant_name = assistant_name
        self.file = file
        self.file = client.files.create(
            file=open(self.file, "rb"),
            purpose='assistants'
        )
        self.assistant = client.beta.assistants.create(
            name=self.assistant_name,
            instructions=get_openai_assistant_instructions(),
            tools=[{"type": "code_interpreter"}],
            model="gpt-4-1106-preview",
            file_ids=[self.file.id],
        )


def call_assistant(assistant, file):
    assistant = Assistant(assistant, file)
    print(assistant.assistant)
