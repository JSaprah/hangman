import random

def welcome():
    """
    Welcome the user to the game.
    """
    print("Welcome to Hangman. What is your name?")
    name = input()
    print(f"I have a word on my mind {name}. Can you guess it?")

def get_random_word():
    """
    Get a random word from the given list
    """
    random_words = ["avenue", "bookworm", "cycle", "duplex", "eardrop", "fuchsia", "galaxy", "hyphen", "injury", "jackpot", "kiosk", "luxury", "matrix", "nowadays", "oxygen", "pneumonia", "quartz", "rhubarb", "scratch", "transplant", "unknown", "vodka", "wizard", "youthful", "zodiac"]
    secret_word = random.choice(random_words)

    return(secret_word)

def get_user_response(word):
    """
    Receive customer response
    """
    turns = 0

    print(word)
    print("Which letter do you think is the the word I am thinking of?")

    while turns < 6:
        user_response = input()
        print(f"You guessed {user_response}.")
        
        if(user_response in word):
            print("Well done. Continue guessing..")
            
        else:
            print("Oops try again")
            turns = turns + 1

        print(turns)

def main():
    """
    Run all program functions
    """
    welcome()
    secret_word = get_random_word()
    get_user_response(secret_word)

main()