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


def create_a_thread():
    return client.beta.threads.create()


def add_message_to_thread(thread_id, content):
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content,
    )


def start_run(thread_id, assistant_id):
    return client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )


def get_messages_and_print(thread_id):
    messages = client.beta.threads.messages.list(
        thread_id=thread_id,
    )
    for message in reversed(messages.data):
        if message.role != "user":
            print_in_color("Assistant: " + message.content[-1].text.value, config.get_info_color())


def summon_assistant():
    assistant_name, file = vars(get_assistant_inputs()).values()

    print_in_color(f"Summoning an assistant...", config.get_info_color())
    assistant = Assistant(assistant_name, file)
    get_user_question = input("Enter your question: ")

    thread = create_a_thread()
    print(f"Thread id: {thread.id}")

    while get_user_question != ":q" or get_user_question != ":quit":
        if get_user_question == ":q" or get_user_question == ":quit":
            print_in_color("Exiting chat mode", config.get_info_color())
            break

        message = add_message_to_thread(thread.id, get_user_question)
        print(f"Message id: {message.id}")

        run = start_run(thread.id, assistant.assistant.id)
        print(f"Run id: {run.id} | Run status: {run.status}")

        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            time.sleep(1)

        get_messages_and_print(thread.id)
        get_user_question = input("Enter your question: ")
