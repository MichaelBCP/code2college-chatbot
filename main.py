import random
import gemini_api
from gemini_api import answer_query


def menu():
    print("--------------------------------------------------------------")
    print("Thank you for visiting the DMV today, please choose an option: ")
    print("1) Get license")
    print("2) Take driving test")
    print("3) Speak to an associate")
    print("--------------------------------------------------------------")

def get_license():
    #number-letter-letter-letter-number-number-number format

    #Letters for license plate
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M")

    license_number = (
            str(random.randint(0, 9)) +
            random.choice(letters) +
            random.choice(letters) +
            random.choice(letters) +
            str(random.randint(0, 9)) +
            str(random.randint(0, 9)) +
            str(random.randint(0, 9))
    )

    print("Your license number is "+license_number+ " it will be delivered shortly")

#questions sourced from DMV website
questions = {
    "When is it legal to drive off the road to pass another vehicle? A) Always B) Never": "B",
    "What should you do when there is a school bus ahead that starts flashing yellow warning lights? A) Speed up B) Stop Immediately C) Slow down and prepare to stop": "C",
}

def take_driving_test():
    score = 0

    for question in questions:
        answer = input(question)
        if answer == questions[question]:
            score += 1

    if score == 2:
        print("Congrats you passed!")
    elif score == 1:
        print("Almost, try again later!")
    else:
        print("Study harder next time!")

def ask_ai():
    question = input("What would you like to ask the associate?: ")
    print(answer_query(question, "You are a DMV associate to help out customers"))


def main():
    while True:
        menu()
        action = input(": ")
        if action == "1":
            get_license()
        elif action == "2":
            take_driving_test()
        elif action == "3":
            ask_ai()

main()