# Python program to solve a quadratic equation: ax^2 + bx + c = 0

# Import required modules
import os
import cmath

# ========== Main Program ==========
if __name__ == "__main__":
    # Clear the terminal for a clean interface
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=== Quadratic Equation Solver ===")
    print("Equation form: ax^2 + bx + c = 0\n")

    try:
        # Get coefficients from user
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        # Validate that a is not zero
        if a == 0:
            print("\nInvalid input! 'a' cannot be 0 for a quadratic equation.")
        else:
            # Calculate discriminant
            discriminant = (b ** 2) - (4 * a * c)

            # Calculate both roots
            root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

            # Display result type and roots
            if discriminant > 0:
                print("\nTwo distinct real roots:")
            elif discriminant == 0:
                print("\nOne repeated real root:")
            else:
                print("\nTwo complex roots:")

            print(f"x1 = {root1}")
            print(f"x2 = {root2}")

    except ValueError:
        print("\nInvalid input! Please enter numeric values.")
