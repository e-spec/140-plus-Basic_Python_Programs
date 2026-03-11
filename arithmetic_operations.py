# Python program to perform arithmetical operations: addition, subtraction, multiplication, division, and exponentiation

# Import required module for clearing terminal
import os

# ========== Function Definitions ==========

def addition(a, b):
    """Function to perform addition of two numbers"""
    return a + b

def subtraction(a, b):
    """Function to perform subtraction of two numbers"""
    return a - b

def multiplication(a, b):
    """Function to perform multiplication of two numbers"""
    return a * b

def division(a, b):
    """Function to perform division of two numbers"""
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def exponentiation(a, b):
    """Function to perform exponentiation (a raised to the power of b)"""
    return a ** b

# ========== Main Program ==========
if __name__ == "__main__":
    # Clear the terminal for a clean interface
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display menu options
    print("=== Arithmetic Operations Program ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    
    # Get user choice
    choice = input("\nEnter your choice (1, 2, 3, 4, or 5): ")
    
    # Display the selected operation
    if choice == '1':
        print("Your selection is Addition")
    elif choice == '2':
        print("Your selection is Subtraction")
    elif choice == '3':
        print("Your selection is Multiplication")
    elif choice == '4':
        print("Your selection is Division")
    elif choice == '5':
        print("Your selection is Exponentiation")
    
    # Get numbers from user and validate input
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Perform operation based on choice
        if choice == '1':
            print("\nOperation: Addition")
            result = addition(num1, num2)
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == '2':
            print("\nOperation: Subtraction")
            result = subtraction(num1, num2)
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == '3':
            print("\nOperation: Multiplication")
            result = multiplication(num1, num2)
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == '4':
            print("\nOperation: Division")
            result = division(num1, num2)
            print(f"\nResult: {num1} / {num2} = {result}")
        elif choice == '5':
            print("\nOperation: Exponentiation")
            result = exponentiation(num1, num2)
            print(f"\nResult: {num1} ^ {num2} = {result}")
        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or 5.")
    
    # Handle invalid numeric input
    except ValueError:
        print("Invalid input! Please enter numeric values.")
