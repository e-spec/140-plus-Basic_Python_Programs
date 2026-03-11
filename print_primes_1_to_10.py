# Python Program to Print all Prime Numbers in an Interval of 1-10

import os

os.system('cls' if os.name == 'nt' else 'clear')

start = 1
end = 10

print(f"Prime numbers between {start} and {end} are:")

for number in range(start, end + 1):
    if number > 1:
        is_prime = True

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number)
