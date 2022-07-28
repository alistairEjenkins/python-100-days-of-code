import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
print(data)

nato_letters = {row.letter: row.code for (index, row) in data.iterrows()}

message = input("Enter a word please: ")

nato_message = [nato_letters[letter] for letter in message.upper()]
print(nato_message)
