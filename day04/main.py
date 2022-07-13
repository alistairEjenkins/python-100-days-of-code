# Rock, Paper, Scissors
from random import choice
moves = ['r', 'p', 's']

player_choice = input("What is you choice (r/p/s)? ")
computer_choice = choice(moves)

if player_choice == computer_choice:
    print(f"{player_choice} vs {computer_choice}. It's a tie")
elif player_choice == 'r':
    if computer_choice == 'p':
        print(f"{player_choice} vs {computer_choice}. Computer wins")
    else:
        print(f"{player_choice} vs {computer_choice}. Player wins")
elif player_choice == 'p':
    if computer_choice == 's':
        print(f"{player_choice} vs {computer_choice}. Computer wins")
    else:
        print(f"{player_choice} vs {computer_choice}. Player wins")
else:
    if computer_choice == 'r':
        print(f"{player_choice} vs {computer_choice}. Computer wins")
    else:
        print(f"{player_choice} vs {computer_choice}. Player wins")

# revisit with indexing 2d array