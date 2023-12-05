import os
import time

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

file = client.files.create(
    file=open("../../results.csv", "rb"),
    purpose='assistants'
)

assistant = client.beta.assistants.create(
    name="PerfGPT",
    instructions="Analyse the file and answer questions about performance stats",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview",
    file_ids=[file.id],
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Give me the 95th elapsed time percentile, maximum elapsed time, and minimum elapsed time.",
    # content="""
    # Give me the 95th elapsed time percentile, maximum elapsed time, and minimum elapsed time.
    # Give me unique transactions names, and the number of transactions.
    # Present the number of transactions, and the number of transactions with errors.
    # Also give HTTP error codes, and the number of transactions with HTTP error codes.
    # Everything should be in a table format so that I can understand it.
    # Do not give detailed explanation. If you find any bottleneck, please share that as well.
    # """,
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)

while run.status != "completed":
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    time.sleep(1)

messages = client.beta.threads.messages.list(
    thread_id=thread.id,
)

print(f"M: {messages.data[-1]}")
print("M2: " + messages.data[-1].content[-1].text.value)

for message in reversed(messages.data):
    if message.role != "user":
        print("System message " + message.content[-1].text.value)
    # print("Each message " + message.content[-1].text.value)
