# 1- Import the random module
import random

# 2- creste subject
subjects = [
    "shahrukh khan",
    "virat kohli",
    "Nirmala sitharaman",
    "A Mumbai cat",
    "A group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver form delhi"
]

actions = [
    "lunches",
    "cancels",
    "dance with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL match",
    "at india gate"
]

# 3- start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {places_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

# print Good bye Message
print("\n thanks for using the Fake News Headline Generator. Have a fun Day")