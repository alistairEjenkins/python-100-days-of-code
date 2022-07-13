# treasure map

def print_map():
    print("    1    2    3")
    print(f"1 {row1}\n2 {row2}\n3 {row3}\n")
row1 = ['_', '_', '_']
row2 = ['_', '_', '_']
row3 = ['_', '_', '_']
map = [row1, row2, row3]

print_map()
column = int(input("Which column do you want to bury the treasure in? (1,2, or 3)")) - 1
row = int(input("Which row do you want to bury the treasure in? (1,2, or 3)")) - 1
map[row][column] = '*'
print_map()


