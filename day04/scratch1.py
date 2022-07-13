#  heads or tails
from random import choice
faces = ['heads', 'tails']

print("Tossing the coin ...")
call = input(f"...Call it! {faces[0]} or {faces[1]}... ")
landed_on = choice(faces)
if call == landed_on:
    print(f"{landed_on} it is. You win")
else:
    print(f"Sorry, you lose. It landed on {landed_on}")
