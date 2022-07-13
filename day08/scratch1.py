# paint can calculator
from math import ceil

height = int(input("What is the height of the wall? (m)"))
width = int(input("What is the width of the wall? (m)"))

def cans_needed(height, width, coats=2, coverage=5):

    return ceil(height * width * coats/ coverage)

cans = cans_needed(height,width)
print(f"You will need {cans} cans of paint to cover a {height}m x {width}m wall")