# password generator
from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_of_letters = int(input("How many letters in your password? "))
num_of_numbers = int(input("How many numbers in your password? "))
num_of_symbols = int(input("How many symbols in your password? "))

letter_list = [choice(letters) for _ in range(num_of_letters)]
numbers_list = [choice(numbers) for _ in range(num_of_numbers)]
symbols_list = [choice(symbols) for _ in range(num_of_symbols)]

password = letter_list + numbers_list + symbols_list
shuffle(password)
password = "".join(password)
print(f"Your password: {password}")


