import random


def get_random_word():
    """
    Gets a random word from the list and
    return the secret word
    """
    random_words = [
        "avenue", "bookworm", "cycle", "duplex",
        "eardrop", "fuchsia", "galaxy", "hyphen",
        "injury", "jackpot", "kiosk", "luxury",
        "matrix", "nowadays", "oxygen", "pneumonia",
        "quartz", "rhubarb", "scratch", "transplant",
        "unknown", "vodka", "wizard", "youthful", "zodiac"
        ]

    secret_word = random.choice(random_words)

    return (secret_word)
