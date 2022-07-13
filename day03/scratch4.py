# pizza order service

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L").upper()
add_pepperoni = input("Do you want pepperoni? ").upper()
extra_cheese = input("Do you want extra cheese? ").upper()

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
else:
    bill = 25

if add_pepperoni== 'Y':
    if size == 'S':
        bill +=2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is £{bill}")
