# Python Program to Check if a Number is Odd or Even

import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        number = int(input("Enter an integer: "))

        if number % 2 == 0:
            print("The number is Even.")
        else:
            print("The number is Odd.")

    except ValueError:
        print("Invalid input! Please enter a valid integer value.")

    choice = input("\nDo you want to check another number? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        print("Thank you for using the program!")
        break
