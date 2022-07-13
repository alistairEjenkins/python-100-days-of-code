# bmi calculator

weight = int(input("What is your weight (kg)? "))
height = float(input("What is your height(m)? "))

bmi = weight / height ** 2
print(f"Your BMI is : {bmi}")