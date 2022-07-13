# calculator
from os import system

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

choice = 'f'
answer = None
power_on = True
while power_on:
    if choice == 'f':
        num1 = int(input('Input a number: '))
    else:
        num1 = answer
        print(f"First number : {num1}")
    for op in operations:
        print(op)
    op_choice = input('Choose an operation')
    num2 = int(input("Enter a second number"))
    answer = operations[op_choice](num1, num2)
    print(f"{num1} {op_choice} {num2} = {answer}")
    choice = input("Use (a)nswer in new sum or (f)resh calculation?")
    system('cls')
    if choice == "power off":
        power_on = False
    