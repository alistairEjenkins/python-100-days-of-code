# Love Calculator

def letter_counter(word, names):

    counter = 0
    for letter in word:
        counter += names.count(letter)
    return counter

name1 = input("What is your name? ")
name2 = input("What is the name of the person you fancy? ")

names = name1 + name2

tens = letter_counter('true', names)
units = letter_counter('love', names)

love_count = tens * 10 + units