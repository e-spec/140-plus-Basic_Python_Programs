# Python program to convert Celsius to Fahrenheit and vice versa

# Import required module for clearing terminal
import os

# ========== Function Definitions ==========

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5 / 9

# ========== Main Program ==========
if __name__ == "__main__":
    # Clear the terminal for a clean interface
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display menu options
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    # Get user choice
    choice = input("\nEnter your choice (1 or 2): ")

    # Get temperature from user and validate input
    try:
        temperature = float(input("Enter temperature value: "))

        # Perform conversion based on choice
        if choice == '1':
            result = celsius_to_fahrenheit(temperature)
            print(f"\n{temperature}°C = {result:.2f}°F")
        elif choice == '2':
            result = fahrenheit_to_celsius(temperature)
            print(f"\n{temperature}°F = {result:.2f}°C")
        else:
            print("Invalid choice! Please select 1 or 2.")

    # Handle invalid numeric input
    except ValueError:
        print("Invalid input! Please enter a valid number.")
