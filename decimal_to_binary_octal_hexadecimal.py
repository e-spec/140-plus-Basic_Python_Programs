# Python Program to Convert Decimal to Binary, Octal and Hexadecimal

import os

# Run until user chooses to exit
while True:
    # Clear terminal for a clean screen
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Take decimal integer input from user
        number = int(input("Enter a decimal integer: "))

        # Display converted values
        print(f"\nDecimal: {number}")
        print(f"Binary: {bin(number)}")
        print(f"Octal: {oct(number)}")
        print(f"Hexadecimal: {hex(number)}")

    # Handle invalid (non-integer) input
    except ValueError:
        print("Invalid input! Please enter a valid integer value.")

    # Ask user to continue or exit
    choice = input("\nDo you want to convert another number? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for using the program!")
        break
