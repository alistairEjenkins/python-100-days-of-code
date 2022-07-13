# banker roulette
from random import choice
names = input('Can I have the names of the diners please? \n')
names_list = names.split(',')
choice = choice(names_list)
print(f"{choice} will be paying the bill tonight.")