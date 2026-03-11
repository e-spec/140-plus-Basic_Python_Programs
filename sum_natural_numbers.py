# Python Program to Find the Sum of Natural Numbers

import os

# Run until user chooses to exit
while True:
    # Clear terminal for a clean screen
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Take integer input from user
        number = int(input("Enter a positive integer: "))

        # Validate input
        if number <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            # Calculate sum of natural numbers from 1 to number
            total = number * (number + 1) // 2
            print(f"The sum of natural numbers from 1 to {number} is {total}.")

    # Handle invalid (non-integer) input
    except ValueError:
        print("Invalid input! Please enter a valid integer value.")

    # Ask user to continue or exit
    choice = input("\nDo you want to find another sum? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for using the program!")
        break
