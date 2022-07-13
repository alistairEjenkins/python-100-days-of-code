# secret auction

import os

bids = {}

print("Welcome to the secret auction program")

more_bids = True
while more_bids:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: £"))
    bids[name] = bid
    if input("Any other bids? (y/n)").lower() == 'n':
        more_bids = False
    else:
        os.system('cls')
else:
    highest_bid = 0
    highest_bidder = ''
    for name in bids:
        if bids[name] > highest_bid:
            highest_bidder = name
            highest_bid = bids[name]
    os.system('cls')
    print(f"The winner of the auction is {highest_bidder}, with a bid of £{highest_bid}")


