user_choice_1 = "Give me min, max, 95 percentile, 99 percentile elapsed or response time in a table format."
user_choice_2 = "Analyze the data and give me the bottleneck in a simple sentence."
user_choice_3 = "Give me the passed and failed transactions in a table format."
user_choice_4 = "Give me the HTTP response code split by transaction in a table format."
user_choice_5 = "Give me only the errors in a table format."

openai_assistant_choices = []
for choice in range(1, 5):
    openai_assistant_choices.append(f"user_choice_{choice}")

print(openai_assistant_choices)

user_input = input("Enter your choice: ")
while True:
    if user_input=="exit":
        break
    if user_input=="1":
        print(user_choice_1)
        user_input = input("Enter your choice: ")
    elif user_input=="2":
        print(user_choice_2)
        user_input = input("Enter your choice: ")
    elif user_input=="3":
        print(user_choice_3)
        user_input = input("Enter your2 choice: ")
    elif user_input=="4":
        print(user_choice_4)
        user_input = input("Enter your choice: ")
    elif user_input=="5":
        print(user_choice_5)
        user_input = input("Enter your choice: ")
    else:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice: ")


