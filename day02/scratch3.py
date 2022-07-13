# life in weeks

MAX_AGE = 90 
age = int(input("What is your age?"))

years_left = MAX_AGE - age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"If you live till {MAX_AGE}, will have {days_left} days left to live, or {weeks_left} weeks left to live, or {months_left} months left.")