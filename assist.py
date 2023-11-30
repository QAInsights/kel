import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Give me 95th percentile"
)
file = client.files.create(
  file=open("results.txt", "rb"),
  purpose='assistants'
)
assistant = client.beta.assistants.create(
    name="Data visualizer",
    description="You are a performance engineer. Help a developer.",
    model="gpt-4-1106-preview",
    tools=[{"type": "code_interpreter"}],
    file_ids=[file.id]
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please give me 95th percentile."
)
messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

print(messages)

