# bmi calculator v2

weight = int(input("What is your weight (kg)? "))
height = float(input("What is your height(m)? "))

bmi = weight / height ** 2
print(f"Your BMI is : {bmi}")

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese.")
