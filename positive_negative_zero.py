# Python Program to Check if a Number is Positive, Negative or Zero

import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        number = float(input("Enter a number: "))

        if number > 0:
            print("The number is Positive.")
        elif number < 0:
            print("The number is Negative.")
        else:
            print("The number is Zero.")

    except ValueError:
        print("Invalid input! Please enter a valid numeric value.")

    choice = input("\nDo you want to check another number? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        print("Thank you for using the program!")
        break
