# hangman

from random import choice
import os
import time

def display(lives, secret_word, correct_guesses):

    os.system('cls')
    print("Can you guess my secret word?")
    print(f"You have {lives} lives left.")
    for letter in secret_word:
        if letter in correct_guesses:
            print(f"{letter} ", end='')
        else:
            print("_ ", end='')

word_list = ['apple', 'banana', 'coconut']

secret_word = choice(word_list)
correct_guesses = []
already_chosen = []
print("Welcome to Hangman")
lives = 7
while lives:
    display(lives, secret_word, correct_guesses)
    letter_choice = input("\nPlease choose a letter\n>>")
    if letter_choice in already_chosen:
        print("You have already chosen that letter. Please try again.")
        continue
    else: 
        already_chosen.append(letter_choice)
        if letter_choice in secret_word:
            correct_guesses.append(letter_choice)
            if len(correct_guesses) == len(set(secret_word)):
                print(f"Congratulations you have guessed my secret word, {secret_word}")
                break
        else:
            print(f"Sorry, that is an incorrect guess.")
            lives -= 1
    time.sleep(3)
else:
    print(f"Sorry you lose. The secret word was {secret_word}")




