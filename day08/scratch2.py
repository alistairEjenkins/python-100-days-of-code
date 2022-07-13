# prime number checker
from time import sleep

def is_prime(num):

    if num == 1:
        return "1 is not prime."
    elif num == 2:
        return "2 is prime."
    else:
        for n in range(2,num):
            if num % n == 0:
                return f"{num} is not prime"
        else:
            return f"{num} is prime"
            

for num in range(1,101):
         print(is_prime(num))
         sleep(0.5)

