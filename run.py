import random

random_word = "secret"

def welcome():
    """
    Welcome the user to the game and explaining the rules
    """
    print("Welcome to Hangman. What is your name?")
    name = input()
    print(f"I have a word on my mind {name}. Can you guess it?")

def main():
    """
    Run all program functions
    """
    welcome()

main()