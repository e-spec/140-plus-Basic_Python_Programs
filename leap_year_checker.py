# Python Program to Check Leap Year

import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        year = int(input("Enter a year: "))

        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is Not a Leap Year.")

    except ValueError:
        print("Invalid input! Please enter a valid integer year.")

    choice = input("\nDo you want to check another year? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        print("Thank you for using the program!")
        break
