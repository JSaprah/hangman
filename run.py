import os
from lists.hangman import hangman_display
from lists.words import get_random_word
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def clear_console():
    """
    Clear the console
    """
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)


def welcome():
    """
    Welcome the user to the game.
    """

    print(Fore.CYAN + """
██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ 
██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████ 
                                                                
    """)

    print("Welcome to Hangman.")
    name = input("What is your name?\n").lower().strip(" ")
    clear_console()
    print(f"Are you ready to play {name}?")
    print(Fore.CYAN + "Press i: for instructions")

    menu()


def menu():

    invalid_input = True

    print(Fore.CYAN + "Press p: for play game")
    print(Fore.CYAN + "Press q: for quiet game")

    while invalid_input:

        pressed_key = input("Enter your answer here\n").lower()

        if (pressed_key == "i"):
            invalid_input = False
            instruction()
            return False

        elif (pressed_key == "p"):
            invalid_input = False
            play()
            return False

        elif (pressed_key == "q"):
            main()

        else:
            print("Invalid input. Please select one of the options above")
            invalid_input = True
            clear_console()


def instruction():

    clear_console()
    print("A random word will be represented by a row of dashes")
    print("Your task is to guess the letter you think is in the word")
    print("Each wrong guess will bring the man closer to be hanged")
    print("Do you think you can take the challenge and safe the hanging man?")

    menu()


def play():
    clear_console()
    secret_word = get_random_word()
    validate_user_response(secret_word)


def validate_user_response(word):
    """
    Set the turns to 0 and increase the count if the user makes a wrong guess
    Receive and validate user response
    """
    failed_attempt = 0
    guess = []
    characters = [char for char in word]
    hidden_value = ["_ "] * len(characters)
    hide = "_ " * len(characters)

    char_word = len(characters)

    print("I have a word on my mind.")
    print(f"The word is: {char_word} characters long")
    print("The word I am thinking of is:")
    print(Fore.CYAN + hide)

    while failed_attempt < 8:
        user_response = input("Fill in a letter\n").lower().strip(" ")
        print(f"You guessed {user_response}.")

        if (user_response in guess):
            print(Fore.YELLOW + f"You already guessed these letters {guess}.")
            print("Try again!")

        elif (user_response == ""):
            print(Fore.YELLOW + "blank value not allowed")

        elif (user_response.isalpha() is False):
            print(Fore.YELLOW + "Letter not in the alphabet. Try again!")

        elif (len(user_response) != 1):
            print(Fore.YELLOW + "Input of only one letter required\n")

        elif (user_response in characters):
            print(Fore.GREEN + "Well done. Continue guessing..")
            guess.append(user_response)

            for index, letter in enumerate(characters):
                if letter != "_ " and user_response == letter:
                    hidden_value[index] = letter
            print(Fore.CYAN + "".join(hidden_value))

            if (hidden_value == characters):
                result_win()

        else:
            print(Fore.RED + "Oops try again")
            failed_attempt = failed_attempt + 1
            guess.append(user_response)

            print(Fore.CYAN + hangman_display(failed_attempt))

        print(f"Failed attempts: {failed_attempt}")

    result_fail(word)
    clear_console()


def result_fail(correct_answer):
    """
    Result on fail
    """
    print("You could not safe the man from hanging")
    print(f"The correct answer was {correct_answer}")
    print("Would you like to play again?")
    menu()
    clear_console()


def result_win():
    """
    Result on win
    """
    print("You won")
    print("Would you like to play again?")
    menu()
    clear_console()


def main():
    """
    Run all program functions
    """
    clear_console()
    welcome()


main()
