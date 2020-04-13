"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""

import random

words = "dog cat mouse deer snake".split()

def generate_random_word():
    """
    read a list of words from a file and pick a random one to return
    Skip read list from file
    """
    return str(random.choice(words)).lower()


def print_word(word, guessed_letter):
    newword = ""
    for char in word:
        if char in guessed_letter:
            newword += char
        else:
            newword += "-"
    print(list(newword))


def pick_a_letter():
    input_letters = str(input("pick a letter: "))
    while (len(input_letters) < 1):
        input_letters = input("pick a letter:: ")
    letter = input_letters[:1].lower()
    print(letter, "is picked.")
    return letter


def print_guesses_left(guesses_left):
    print(guesses_left, "choices left")


def all_letter_guessed(word, guessed_letter):
    for char in word:
        if char not in guessed_letter:
            return False
    return True;


def want_to_play():
    i = input("play again? (y or n):")
    return i == "y" or i == "Y"


def print_word(word, guessed_letter):
    newword = ""
    for char in word:
        if char in guessed_letter:
            newword += char
        else:
            newword += "-"
    print(list(newword))
    # return for webapp
    return newword


def play_hangman():
    """ this is the python script version of the game """
    want_to_play = True

    while (want_to_play):
        word = generate_random_word()
        guessed_letters = []
        guesses_left = 6
        letter = pick_a_letter()
        done = False
        while not done:
            if letter in guessed_letters:
                print(letter, "has picked!")
                guesses_left = guesses_left - 1
            elif letter not in word:
                guessed_letters.append(letter)
                print(letter, "is NOT in the word!")
                guesses_left = guesses_left - 1
            else:
                guessed_letters.append(letter)
                print(letter, "is in the word!")
            print_guesses_left(guesses_left)
            if all_letter_guessed(word, guessed_letters):
                print("you won!")
                done = True
            elif guesses_left == 0:
                print("you lost!")
                done = True
            else:
                print_word(word, guessed_letters)
                letter = pick_a_letter()
        want_to_play = input("play again? (y or n):")


if __name__ == '__main__':
    play_hangman()
