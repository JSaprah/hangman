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
    Set the turns to 0 and increase the count if the user makes a wrong guess
    Receive user response
    """
    turns = 0
    guess = []

    characters = [c for c in word]
    print(characters)
    print("Which letter do you think is the the word I am thinking of?")

    while turns < 5:
        user_response = input()
        print(f"You guessed {user_response}.")
        guess.append(user_response)
        print(f"This is the guess{guess}")

        try:
            if(user_response != 1):
                raise ValueError("Exact one value required")
            elif(user_resonse in guess):
                raise ValueError(f"You already guessed these letters {guess}.")
        except ValueError as e:
            print("Please provide a different input")
            correct_value = False

        if(user_response in characters):
            print("Well done. Continue guessing..")
            
        else:
            print("Oops try again")
            turns = turns + 1
            print_hangman(turns)
            print ("_",end="")

        print(turns)

def main():
    """
    Run all program functions
    """
    welcome()
    secret_word = get_random_word()
    get_user_response(secret_word)

def print_hangman(turns):
    """
    Print the hangman images on each wrong guess
    """

    if(turns == 6):
        print("----------")
        print("|    0")
        print("|   \|/")
        print("|   / \ ")

main()