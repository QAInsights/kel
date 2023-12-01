import os
import time

from inputs import get_assistant_inputs

from openai import OpenAI

import get_configs as config
from utils import print_in_color

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
            instructions=config.get_openai_assistant_instructions(),
            tools=[{"type": "code_interpreter"}, {"type": "retrieval"}],
            model="gpt-4-1106-preview",
            file_ids=[self.file.id],
        )


def summon_assistant():
    assistant_name, file = vars(get_assistant_inputs()).values()

    print_in_color(f"Summoning an assistant...", config.get_info_color())
    assistant = Assistant(assistant_name, file)
    get_user_question = input("Enter your question: ")

    while get_user_question != ":q" or get_user_question != ":quit":
        if get_user_question == ":q" or get_user_question == ":quit":
            print_in_color("Exiting chat mode", config.get_info_color())
            break

        # Create a thread
        thread = client.beta.threads.create()

        # Create a message
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=get_user_question,
        )

        # Create a run
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.assistant.id,
        )

        # Wait for the run to complete
        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            time.sleep(1)

        # List the messages
        messages = client.beta.threads.messages.list(
            thread_id=thread.id,
        )

        # Print the messages
        for message in reversed(messages.data):
            print(message.content[0].text.value)

        get_user_question = input("Enter your question: ")



