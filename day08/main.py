# caesar cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(direction, text, shift):

    if direction == 'decode':
        shift *= -1

    caeser_text = ''

    for letter in text:
        if letter not in alphabet:
            caeser_text += letter
        else:
            new_index = (alphabet.index(letter) + shift) % len(alphabet)
            caeser_text += alphabet[new_index]
    
    return caeser_text

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(f"{caeser(direction, text, shift)}\n")
    another_message = input("Do you want to caesar cipher another message? (Y/n) ")
    if another_message == 'n':
        break
