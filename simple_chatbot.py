"""A simple chatbot that respond to user inputs with predefined answers"""
from random import choice
import platform
import sys

def main():
    jokes = [
    "Why do Java developers wear glasses? Because they don’t C#.",
    "A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?'",
    "How many programmers does it take to change a light bulb? None. That’s a hardware problem.",
    "What’s a programmer’s favorite hangout place? The foo bar.",
    "I told my computer I needed a break... Now it won’t stop sending me KitKat ads."
    ]
    # Predefined questions and their responses

    print("Welcome to the Simple Chatbot!")
    name = input("Enter your name to continue: ")
    print(f"Hello {name.title()}!")

    while True:
        print("Here are some questions you can ask me")

        questions =[("How are you?","I'm fine, thank you!"), ("What is your name?","My name is Chatbot."), ("Tell me a joke",choice(jokes)), ("What is your favorite programming language?", "I love Python!")]

        for i, question in enumerate(questions, start=1):
            print(f"{i}. {question[0]}")
        
        user_choice = get_user_choice()
        if user_choice == 1:
            print(questions[0][1])
        elif user_choice == 2:
            print(questions[1][1])
        elif user_choice == 3:
            print(questions[2][1])
        elif user_choice == 4:
            print(questions[3][1])
        
        print("\nPress x to exit the chatbot or any other key to continue:")
        if get_single_char() == "x":
            print("Exiting the chatbot.")
            return


def get_user_choice():
    while True:
        try:
            user_choice  = int(input("Enter your choice (1-4): "))
            if user_choice in [1, 2, 3, 4]:
                return user_choice
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        except KeyboardInterrupt:   
            print("\nExiting the chatbot.")
            exit()
    

def get_single_char():
    if platform.system() == "Windows":
        import msvcrt
        return msvcrt.getch().decode()
    else:
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch


if __name__ == "__main__":
    main()