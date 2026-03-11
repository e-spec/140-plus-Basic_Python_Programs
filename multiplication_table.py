# Python Program to Display the Multiplication Table

import os

# Run until user chooses to exit
while True:
    # Clear terminal for a clean screen
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Take integer input from user
        number = int(input("Enter an integer to display its multiplication table: "))

        print(f"\nMultiplication Table of {number}:\n")

        # Display table from 1 to 10
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")

    # Handle invalid (non-integer) input
    except ValueError:
        print("Invalid input! Please enter a valid integer value.")

    # Ask user to continue or exit
    choice = input("\nDo you want to display another table? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for using the program!")
        break
