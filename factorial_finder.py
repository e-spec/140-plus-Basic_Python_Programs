# Python Program to Find the Factorial of a Number

import os

# Run until user chooses to exit
while True:
    # Clear terminal for a clean screen
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Take integer input from user
        number = int(input("Enter a non-negative integer: "))

        # Validate input
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            # Calculate factorial
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i

            print(f"The factorial of {number} is {factorial}.")

    # Handle invalid (non-integer) input
    except ValueError:
        print("Invalid input! Please enter a valid integer value.")

    # Ask user to continue or exit
    choice = input("\nDo you want to find another factorial? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for using the program!")
        break
