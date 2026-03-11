# Python program to convert kilometers to miles

# Import required module for clearing terminal
import os

# ========== Function Definition ==========

def km_to_miles(kilometers):
    """Function to convert kilometers to miles"""
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles

# ========== Main Program ==========
if __name__ == "__main__":
    # Clear the terminal for a clean interface
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display program title
    print("=== Kilometers to Miles Converter ===\n")
    
    # Get input from user and validate
    try:
        # Get kilometers from user
        kilometers = float(input("Enter distance in kilometers: "))
        
        # Validate input
        if kilometers < 0:
            print("Error: Distance cannot be negative!")
        else:
            # Convert kilometers to miles
            miles = km_to_miles(kilometers)
            
            # Display result
            print(f"\n{kilometers} km = {miles:.2f} miles")
    
    # Handle invalid numeric input
    except ValueError:
        print("Invalid input! Please enter a valid number.")
