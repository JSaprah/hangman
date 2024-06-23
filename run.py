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

def validate_user_response(word):
    """
    Set the turns to 0 and increase the count if the user makes a wrong guess
    Receive and validate user response
    """
    turns = 0
    guess = []
    characters = [c for c in word]
    hidden_value = ["_ "] * len(characters)
    hide = "_ " *len(characters)
    print(f"The word I am thinking of is: {hide}")
    
    print(characters)
    
    print("Which letter do you think is the the word I am thinking of?")

    while turns < 5:
        user_response = input()
        print(f"You guessed {user_response}.")

        if(user_response in guess):
            print(f"You already guessed these letters {guess}. Try again!")

        elif(user_response not in "a,b,c,d,e,f,g,hi,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"):
            print("Letter not in the alphabet. Try again!")

        elif(user_response in characters):
            print("Well done. Continue guessing..")
            guess.append(user_response)

            for i, letter in enumerate(characters):
                if letter != "_ " and user_response == letter:
                    hidden_value[i] = letter
            print("".join(hidden_value))

        else:
            print("Oops try again")
            turns = turns + 1
            guess.append(user_response)

        print(turns)

def main():
    """
    Run all program functions
    """
    welcome()
    secret_word = get_random_word()
    validate_user_response(secret_word)

main()