import sys
from random import choice

def main():
    game_choices =["Rock", "Paper", "Scissors"]
    
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        print("Choose your weapon:")
        for i, choice in enumerate(game_choices, start=1):
            print(f"{i}. {choice}")
        print("4. Quit")
        print()

        user_choice = get_users_choice()
        if user_choice == 4:
            print("Thanks for playing!")
            sys.exit()

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice} ({game_choices[computer_choice - 1]})")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
            (user_choice == 2 and computer_choice == 1) or \
            (user_choice == 3 and computer_choice == 2):
            print("You win!")
        else:
            print("You lose!")
        
        print('\n')



def get_users_choice():
    while True:
        try:
            user_choice = int(input("Enter your choice (1-4): "))
            if user_choice in [1, 2, 3, 4]:
                return user_choice
            else:
                raise ValueError
                
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.", file=sys.stderr)

def get_computer_choice():
    return choice([1,2,3])

if __name__ == "__main__":
    main()