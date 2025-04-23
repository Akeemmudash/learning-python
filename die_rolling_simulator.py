"""A program that simulates rolling a six-sided die and displays the result"""

from random import randint
from simple_chatbot import get_single_char 

def roll_die():
    return randint(1, 6)


def main():
    print("🎲 Welcome to the Die Roll Simulator!\n")

    while True:
        print("Press 'Enter' to roll the die, or press 'X' to quit.")

        key = get_single_char()

        if key in ["\r", '\n']:
            print(f"You rolled a {roll_die()}!")
        elif key.lower() == 'x':
            print("Exiting application 💔...")
            break
        else: 
            print("Invalid Input. Print 'Enter' to roll or 'X' to quit.")

if __name__ == "__main__":
    main()

