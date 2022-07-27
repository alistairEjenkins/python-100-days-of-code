
with open('Input/Letters/starting_letter.txt') as start_letter_file:
    start_letter = start_letter_file.read()

with open('Input/Names/invited_names.txt') as names_file:
    names_list = names_file.readlines()
    names_list = [name.strip() for name in names_list]

for name in names_list:
    named_letter = start_letter.replace('[name]', f'{name}')
    with open(f"Output/ReadyToSend/{name}.txt", 'w') as final_letter:
        final_letter.write(named_letter)
