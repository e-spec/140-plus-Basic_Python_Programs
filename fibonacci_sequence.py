# The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones, 
# typically starting with 0 and 1. 
# So, the sequence begins with 0 and 1, 
# and the next number is obtained by adding the previous two numbers. 
# This pattern continues indefinitely, generating a sequence that looks like this:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.

# Python Program to Print the Fibonacci Sequence

import os

# Run until user chooses to exit
while True:
    # Clear terminal for a clean screen
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Take number of terms from user
        terms = int(input("Enter the number of terms: "))

        # Validate input
        if terms <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            first = 0
            second = 1

            print(f"\nFibonacci sequence up to {terms} terms:\n")

            for _ in range(terms):
                print(first, end=" ")
                next_number = first + second
                first = second
                second = next_number

            print()

    # Handle invalid (non-integer) input
    except ValueError:
        print("Invalid input! Please enter a valid integer value.")

    # Ask user to continue or exit
    choice = input("\nDo you want to print another Fibonacci sequence? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for using the program!")
        break
