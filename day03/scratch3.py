# leap year calculator

#year = int(input("Enter a year: "))

def leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and not year % 400 == 0:
            print(f'{year} : not a leap year')
        else:
            print(f'{year} : is a leap year')
    else:
        print(f"{year} : not a leap year")

for yr in range(1900, 2001):
    leap(yr)
