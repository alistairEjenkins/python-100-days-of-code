# blackjack
from locale import delocalize
from random import choice
from os import system


players_hand = []
dealers_hand = []

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def calculate_score (hand, player=False):

    score = 0
    for card in hand:
        if player and card == 11:
            if input('Play ace as soft ace? y/n ').lower() == 'y':
                card = 1
        score += card
    return score

players_hand.append(deal_card())
players_hand.append(deal_card())
dealers_hand.append(deal_card())
dealers_hand.append(deal_card())
player_bust = False
dealer_bust = False

building_players_hand = True
while building_players_hand:
    print(f"Your cards: {players_hand}")
    print(f"Dealer's first card {dealers_hand[0]}")
    player_score = calculate_score(players_hand, player = True)
    print(f"Your score : {player_score}")
    if player_score > 21:
        print("You are bust!\n")
        player_bust = True
        building_players_hand = False
    else:
        player_action = input("Type 'h' to hit; type 's' to stand: ")
        if player_action == 'h':
            players_hand.append(deal_card())
        else:
            system('cls')
            building_players_hand = False

building_dealers_hand = True
while building_dealers_hand:
    print(f"Your cards: {players_hand}")
    print(f"Dealers cards: {dealers_hand}")
    dealers_score = calculate_score(dealers_hand)
    print(f"Dealer's score: {dealers_score}")
    if player_bust:
        print("Dealer wins")
        building_dealers_hand = False
    else:
        if dealers_score > 21:
            print("I'm bust - you win!")
            dealer_bust = True
            building_dealers_hand = False
        elif dealers_score > 17:
            print("Always stand on 17plus")
            building_dealers_hand = False
        else:
            print("Always hit on 16 or under")
            dealers_hand.append(deal_card())

if not (player_bust or dealer_bust):
    if player_score == dealers_score:
        print("It's a tie!")
    elif player_score > dealers_score:
        print("You win!")
    else:
        print("Dealer wins!")


        


