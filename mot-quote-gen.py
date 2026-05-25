import random
print("Motivational Quote Generator:")

quotes = [
    "The way to get started is to quit talking and begin doing.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "You don't have to see the whole staircase, just take the first step.",
    "A year from now you may wish you had started today.",
    "Action eliminates doubt."

]

while True:
    user_input = input("Press ENTER for a quote or type q to quit: ")
    if user_input == "q":
        print("Goodbye!")
        break

    random_quote = random.choice(quotes)

    print("\n" + random_quote + "\n")
