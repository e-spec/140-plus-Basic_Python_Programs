"""
Calculate the natural logarithm (ln) of a positive number.

Usage:
    python natural_logarithm.py

The program prompts for a number, validates it is positive, and prints ln(number).
The program clears the screen when it starts and clears the screen again
after the user presses Enter to exit.
"""
import math
import os


def main() -> None:
    """Prompt the user for a positive number and print its natural logarithm.

    Steps:
    - Read input as string and strip whitespace.
    - Convert to `float`, handling invalid numeric input.
    - Validate the number is > 0 (ln undefined for non-positive values).
    - Compute `math.log(num)` and print the result.
    """

    # Clear the terminal screen (cross-platform)
    def clear_screen() -> None:
        """Clear the terminal screen on Windows and POSIX systems."""
        os.system("cls" if os.name == "nt" else "clear")

    # Wait for the user to acknowledge then clear the screen
    def pause_and_clear() -> None:
        """Pause for Enter key, then clear the screen before exiting."""
        try:
            input("\nPress Enter to exit...")
        except EOFError:
            # In non-interactive environments, input() may raise EOFError.
            pass
        clear_screen()

    # Main loop: perform calculation, then ask whether to calculate another
    while True:
        # Clear screen at the start of each run
        clear_screen()

        # Read input from the user and try to convert to float
        try:
            s = input("Enter a positive number: ").strip()
            num = float(s)
        except ValueError:
            # Non-numeric input will raise ValueError on conversion
            print("Invalid input. Please enter a numeric value.")
            # Ask whether to try again
            try:
                again = input("Calculate another? (y/n): ").strip().lower()
            except EOFError:
                again = "n"
            if again.startswith("y"):
                continue
            else:
                pause_and_clear()
                break

        # Natural logarithm is only defined for positive numbers
        if num <= 0:
            print("Natural logarithm undefined for zero or negative numbers.")
            try:
                again = input("Calculate another? (y/n): ").strip().lower()
            except EOFError:
                again = "n"
            if again.startswith("y"):
                continue
            else:
                pause_and_clear()
                break

        # Compute the natural logarithm using the math module
        ln = math.log(num)

        # Display the result with a simple explanatory message
        print(f"The natural logarithm (ln) of {num} is {ln}")

        # Ask the user whether to calculate another value
        try:
            again = input("Calculate another? (y/n): ").strip().lower()
        except EOFError:
            again = "n"

        if again.startswith("y"):
            continue
        else:
            pause_and_clear()
            break


if __name__ == "__main__":
    # Run the main function when executed as a script
    main()
