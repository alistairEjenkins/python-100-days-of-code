# number guessing game
from random import randint

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")
if input("Choose a difficulty. Type 'easy' or 'hard'") == 'easy':
    lives = 10
else: 
    lives = 5

secret_number = randint(1,100)
while lives:
    print(f"You have {lives} attempts to guess the number.")
    guess = int(input("Make a guess:"))
    if guess == secret_number:
        print(f"Congratulations! You guessed my secret number, {secret_number} with {lives} left")
        break
    elif guess < secret_number:
        print("Too low!")
    else:   
        print("Too high!")
    lives -= 1
else:
    print(f"You ran out of guesses, the secret number was {secret_number}")