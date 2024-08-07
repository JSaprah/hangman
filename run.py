import os
from lists.hangman import hangman_display
from lists.words import get_random_word
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def clear_console():
    """
    Clears the console and is called from several functions within the program
    """
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)


def welcome():
    """
    Welcomes the user to the game
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

    while len(name) == 0:
        print(Fore.RED + "Nice try, but really")
        name = input("What is your name?\n").lower().strip(" ")
        clear_console()

    clear_console()
    print(Fore.WHITE + f"Are you ready to play {name}?")
    print(Fore.CYAN + "Press i: for instructions")

    menu()


def menu():
    """
    Shows the menu options and
    navigates to the correct function based on user input
    """
    invalid_input = True

    while invalid_input:

        print(Fore.CYAN + "Press p: for play game")
        print(Fore.CYAN + "Press q: for quit game")

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
            clear_console()
            print(Fore.RED + "Invalid input. Please select one of the options")
            print(Fore.CYAN + "Press i: for instructions")
            invalid_input = True


def instruction():
    """
    Shows the guidelines to play the game and
    navigates back to menu
    """
    clear_console()
    print("A random word will be represented by a row of dashes")
    print("Your task is to guess the letter you think is in the word")
    print("Each wrong guess will bring the man closer to be hanged")
    print("Do you think you can take the challenge and safe the hanging man?")

    menu()


def play():
    """
    Triggers the function get_random_word
    Triggers the validate_user_response function
    """
    clear_console()
    secret_word = get_random_word()
    validate_user_response(secret_word)


def validate_user_response(word):
    """
    Receives and validates the user response
    on several conditions
    """
    failed_attempt = 0
    guess = []
    characters = [char for char in word]
    hidden_value = ["_ "] * len(characters)

    char_word = len(characters)

    while failed_attempt < 9:
        print(Fore.CYAN + hangman_display(failed_attempt))
        print("I have a word on my mind.")
        print(f"The word is: {char_word} characters long")
        print("The word I am thinking of is:")
        print(Fore.CYAN + "".join(hidden_value))
        user_response = input("Fill in a letter\n").lower().strip(" ")
        print(f"You guessed {user_response}.")

        if (user_response in guess):
            clear_console()
            print(Fore.YELLOW + f"You already guessed these letters {guess}.")
            print("Try again!")

        elif (user_response == ""):
            clear_console()
            print(Fore.YELLOW + "blank value not allowed")

        elif (user_response.isalpha() is False):
            clear_console()
            print(Fore.YELLOW + "Letter not in the alphabet. Try again!")

        elif (len(user_response) != 1):
            clear_console()
            print(Fore.YELLOW + "Input of only one letter required\n")

        elif (user_response in characters):
            clear_console()
            print(Fore.GREEN + "Well done. Continue guessing..")
            guess.append(user_response)

            for index, letter in enumerate(characters):
                if letter != "_ " and user_response == letter:
                    hidden_value[index] = letter

            if (hidden_value == characters):
                result_win = True
                result(result_win, failed_attempt, word)

        else:
            clear_console()
            print(Fore.RED + "Oops try again")
            failed_attempt = failed_attempt + 1
            guess.append(user_response)

        print(f"Failed attempts: {failed_attempt}")

    result_win = False
    result(result_win, failed_attempt, word)


def result(result_game, attempt, correct_answer):
    """
    Shows the user if he/she won and what the correct answer is
    """
    clear_console()

    if (result_game):

        print(
            Fore.GREEN +
            """
░█░█░█▀█░█░█░░░█░█░█▀█░█▀█
░░█░░█░█░█░█░░░█▄█░█░█░█░█
░░▀░░▀▀▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀
            """)
    else:

        print(
            Fore.RED +
            """
░█░█░█▀█░█░█░░░█░░░█▀█░█▀▀░▀█▀
░░█░░█░█░█░█░░░█░░░█░█░▀▀█░░█░
░░▀░░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░░▀░
            """)

        print("You could not safe the man from hanging")

    print("The correct answer is: ")
    print(Fore.CYAN + correct_answer)

    print(f"Total failed attempts: {attempt}")
    print(Fore.CYAN + hangman_display(attempt))
    print("Would you like to play again?")
    print(Fore.CYAN + "Press i: for instructions")
    menu()


def main():
    """
    Single point of entry to run the program
    """
    clear_console()
    welcome()


main()
