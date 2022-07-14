# higher / lower game
from game_data import data
from random import choice
from os import system

def correct_choice(selection_a, selection_b, choice):

    if choice == 'A':
        return selection_a['follower_count'] > selection_b['follower_count']
    else:
        return selection_b['follower_count'] > selection_a['follower_count']

def choose_b(previous_a, a):

    b = choice(data)
    while b == a or b == previous_a:
        b = choice(data)
    return b

print("Welcome to the Higher/Lower Game")


playing = True
first_round = True
score = 0
while playing:
    if first_round:
        a = choice(data)
        previous_a = None
    else:
        previous_a = a
        a = b
    print(f"Compare A: {a['name']} a {a['description']}, from {a['country']}")
        
    print('VS')
    b = choose_b(previous_a, a)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']} ")
    player_choice = input("Who has the most followers? Type 'A' or 'B':").upper()
    if correct_choice(a, b, player_choice):
        score +=1
        print(f"You are correct! Current score: {score}")
        first_round = False
    else:
        print(f"Sorry, that is incorrect. Your final score is {score}")
        playing = False
    



