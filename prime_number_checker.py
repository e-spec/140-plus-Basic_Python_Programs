# Python Program to Check Prime Number

import os

# Run until user chooses to exit
while True:
    # Clear terminal for a clean screen
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Take integer input from user
        number = int(input("Enter an integer: "))

        # Prime number check logic
        if number <= 1:
            print(f"{number} is Not a Prime Number.")
        else:
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(f"{number} is a Prime Number.")
            else:
                print(f"{number} is Not a Prime Number.")

    # Handle invalid (non-integer) input
    except ValueError:
        print("Invalid input! Please enter a valid integer value.")

    # Ask user to continue or exit
    choice = input("\nDo you want to check another number? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        print("Thank you for using the program!")
        break
