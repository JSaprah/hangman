import random
import os
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_words')


def welcome():
    """
    Welcome the user to the game.
    """

    print("""
██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ 
██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████ 
                                                                
    """)

    print("Welcome to Hangman. What is your name?")
    name = input()
    print(f"Are you ready to play {name}?")

    menu()


def menu():

    invalid_input = True

    while invalid_input:
        print("Press i: for instructions")
        print("Press p: for play game")
        pressed_key = input()
        print(f"Key pressed= {pressed_key}")

        if (pressed_key == "i"):
            invalid_input = False
            instruction()
            return False

        elif (pressed_key == "p"):
            invalid_input = False
            play()
            return False

        else:
            print("input not recognized. What do you want to do?")
            invalid_input = True


def instruction():

    print("A random word will be represented by a row of dashes")
    print("Your task is to guess the letter you think is in the word")
    print("Each wrong guess will bring the man closer to be hanged")
    print("Do you think you can take the challenge and safe the hanging man?")
    print("Enter p if you want to start playing the game")
    print("Enter any key to go back to the menu")

    action_user = input()

    if (action_user == "p"):
        clear_console()
        play()

    else:
        "Returning you back to the menu"
        clear_console()
        menu()


def play():
    secret_word = get_random_word()
    validate_user_response(secret_word)


def get_random_word():
    """
    Get a random word from the given list
    """
    random_words = [
        "avenue", "bookworm", "cycle", "duplex",
        "eardrop", "fuchsia", "galaxy", "hyphen",
        "injury", "jackpot", "kiosk", "luxury",
        "matrix", "nowadays", "oxygen", "pneumonia",
        "quartz", "rhubarb", "scratch", "transplant",
        "unknown", "vodka", "wizard", "youthful", "zodiac"]

    # data = SHEET.worksheet('words')
    # random_words = data.get_all_values()
    secret_word = random.choice(random_words)

    return (secret_word)


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

    print("I have a word on my mind. Can you guess it?")
    print(f"The word I am thinking of is: {hide}")

    print(characters)

    print("Which letter do you think is the the word I am thinking of?")

    while failed_attempt < 5:
        user_response = input()
        print(f"You guessed {user_response}.")

        if (user_response in guess):
            print(f"You already guessed these letters {guess}. Try again!")

        elif (user_response == ""):
            print("blank value not allowed")

        elif (user_response.isalpha() is False):
            print("Letter not in the alphabet. Try again!")

        elif (user_response in characters):
            print("Well done. Continue guessing..")
            guess.append(user_response)

            for index, letter in enumerate(characters):
                if letter != "_ " and user_response == letter:
                    hidden_value[index] = letter
            print("".join(hidden_value))

        else:
            print("Oops try again")
            failed_attempt = failed_attempt + 1
            guess.append(user_response)

        print(f"Failed attempts: {failed_attempt}")

    if (failed_attempt == 5):
        print("You could not safe the man from hanging")
        clear_console()
        print("Would you like to play again?")
        menu()


def clear_console():
    """
    Clear the console
    """
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)


def main():
    """
    Run all program functions
    """
    welcome()


main()