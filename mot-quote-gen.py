import random

print("=" * 50)
print("        MOTIVATIONAL QUOTE GENERATOR")
print("=" * 50)

quotes = [
    "The way to get started is to quit talking and begin doing.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "You don't have to see the whole staircase, just take the first step.",
    "A year from now you may wish you had started today.",
    "Action eliminates doubt.",
    "Dream big. Start small. Act now.",
    "Discipline is choosing what you want most over what you want now.",
    "Hard work beats talent when talent doesn't work hard.",
    "Don't watch the clock; do what it does. Keep going.",
    "Believe you can and you're halfway there.",
    "Great things never come from comfort zones.",
    "Small progress is still progress.",
    "Your only limit is your mind.",
    "Do something today your future self will thank you for.",
    "Success begins with self-belief.",
    "Stay patient and trust your journey.",
    "Failure is another step toward success.",
    "Every expert was once a beginner.",
    "Consistency creates results.",
    "The best view comes after the hardest climb.",
    "Keep showing up even when it's difficult.",
    "Don't stop until you're proud.",
    "Be stronger than your excuses.",
    "Focus on progress, not perfection.",
    "Work hard in silence. Let success make the noise.",
    "You are capable of amazing things.",
    "Stay hungry. Stay humble.",
    "Push yourself because no one else will do it for you.",
    "Your future is created by what you do today.",
    "Success is earned, not given.",
    "Confidence comes from preparation.",
    "The pain of discipline is less than the pain of regret.",
    "Fall seven times, stand up eight.",
    "One step every day adds up.",
    "Don't fear failure. Fear never trying.",
    "Difficult roads often lead to beautiful destinations.",
    "Your mindset determines your future.",
    "Every day is a chance to improve.",
    "Believe in your potential.",
    "Never give up on your goals."
]

quotes_seen = 0

while True:
    user_input = input(
        "\nPress ENTER for a quote or type 'q' to quit: ").lower()

    if user_input == "q":
        print(f"\nYou viewed {quotes_seen} quote(s).")
        print("Keep chasing your goals. Goodbye!")
        break

    random_quote = random.choice(quotes)
    quotes_seen += 1

    print("\nQuote #" + str(quotes_seen))
    print("-" * 50)
    print(random_quote)
    print("-" * 50)
