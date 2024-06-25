# **Hangman**

## **Introduction**

Hangman is a guessing game in which the user has to guess the word by providing letters. The game starts with all dashes. On each correct guess the dash will be replaced by the letter provided by the user. Each wrong guess will increase the failed attempts.

## **The process**

## **Libraries**

## **Functions**

### **Welcome**

* Welcomes the user to the Hangman game with a personalised message
* ASCII art is used to make the game more appealing. The following link has been used:

[ASCII Art](https://textkool.com/en/ascii-art-generator?hl=default&vl=default&font=Lil%20Devil&text=Hangman)

* The ASCII art color has been changed by importing the colorama library. The forground color has been imported.

### **Menu**

* Gives the user two options: read instruction or directly play game. 
* User can either provide i or p as an input. If the input is different than these two options the user will be looped around to answer the question with one these options only. For this part a while loop has been made and the invalid_response variable has been set to True. This value changes if the correct response has been provided.

### **Instruction**

* In this function some print statement are written to print the instructions.
* The user gets the option to start playing the game or navigate back to the menu. 

### **Play**

* Runs the following two functions:
    * secret_word = get_random_word()
    * validate_user_response(secret_word)

### **get_random_word**

* Provides a list of words for the game
* Returns one random word from the list above as the secret_word

### **validate_user_response**

* Takes the secret word as a parameter.

### **clear_console**

* Function written to clear the console to keep the output clean.
* Function used throughout the code were the need is.
* The code behind this function comes from: [Delftstack](https://www.delftstack.com/howto/python/python-clear-console/)

## **Styling**


### **Errors**

* After changing the colors with "colorama fore" the next line took over the same color. I did not want this to happen and avoid retyping the same code. After some Google research I added colorama.init(autoreset=True) to the code. Because of this I was able to make sure that the styling does not go automatically to the next line.

For this part I have used the url:

[Colorama](https://pypi.org/project/colorama/)















## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.
