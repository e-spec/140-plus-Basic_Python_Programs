# Python Program to Find ASCII Value of a Character

import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    character = input("Enter a single character: ")

    if len(character) == 1:
        print(f"The ASCII value of '{character}' is {ord(character)}.")
    else:
        print("Invalid input! Please enter exactly one character.")

    choice = input("\nDo you want to check another character? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        print("Thank you for using the program!")
        break
