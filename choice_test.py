import random

user_choice_1 = "Give me min, max, 95 percentile, 99 percentile elapsed or response time in a table format."
user_choice_2 = "Analyze the data and give me the bottleneck in a simple sentence."
user_choice_3 = "Give me the passed and failed transactions in a table format."
user_choice_4 = "Give me the HTTP response code split by transaction in a table format."


openai_response_prefix = ["Thinking...", "Crunching...", "Analyzing...",
                          "Processing...", "Calculating...", "Working...",
                          "Cooking", "Slicing...", "Dicing...", "Chopping..."]

print(f"""
    random.choice(openai_response_prefix): {random.choice(openai_response_prefix)}
""")
openai_assistant_choices = []
for choice in range(1, 5):
    openai_assistant_choices.append(f"user_choice_{choice}")

choices = {
    1: openai_assistant_choices[0],
    2: openai_assistant_choices[1],
    3: openai_assistant_choices[2],
    4: openai_assistant_choices[3],
}

user_input = input("Enter your choice: ")
while True:
    if user_input == "exit":
        break

    if user_input.strip().isdigit() and int(user_input.strip()) in choices:
        print(openai_assistant_choices[int(user_input.strip()) - 1])
        user_input = input("Enter your choice: ")
        continue
    if user_input.strip().isdigit() and int(user_input.strip()) not in choices:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice: ")
        continue
    else:
        print(user_input)
        user_input = input("Enter your choice: ")
        continue
