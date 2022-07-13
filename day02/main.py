# tip calculator

print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? £"))
number_of_diners = input("How many people to split the bill? ")
tip = input("What percentage would you like to give? 10, 12, or 15? ")

total_bill *= (100 + int(tip)) / 100
split = total_bill / int(number_of_diners)

print(f"Each person should pay: £{split:.2f}")