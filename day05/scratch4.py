# fizz buzz

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print('Fizz-buzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)