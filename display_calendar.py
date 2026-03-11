# Python program to display a calendar

# Import required modules
import os
import calendar

# ========== Main Program ==========
if __name__ == "__main__":
    # Clear the terminal for a clean interface
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=== Calendar Display Program ===\n")

    while True:
        try:
            # Get year and month from user
            year = int(input("Enter year (e.g., 2026): "))
            month = int(input("Enter month (1-12): "))

            # Validate month
            if month < 1 or month > 12:
                print("\nInvalid month! Please enter a value between 1 and 12.\n")
            else:
                # Display calendar
                print("\n", calendar.month(year, month))
                
                # Ask user if they want to continue
                choice = input("Do you want to view another calendar? (yes/no): ").lower()
                if choice not in ['yes', 'y']:
                    print("Thank you for using the Calendar Display Program!")
                    break
                print()

        except ValueError:
            print("\nInvalid input! Please enter numeric values for year and month.\n")
