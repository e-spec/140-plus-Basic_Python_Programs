"""
Calculate logarithms (logaritmos) of a positive number with selectable base.

Usage:
    python logaritmos.py

Features:
 - Clears the screen at start and before exit
 - Supports natural (e), base 10, or a custom base
 - Validates numeric input and base constraints (base > 0 and base != 1)
 - Asks whether to calculate another value
"""
import math
import os


def clear_screen() -> None:
    """Clear the terminal screen on Windows and POSIX systems."""
    os.system("cls" if os.name == "nt" else "clear")


def pause_and_clear() -> None:
    """Pause for Enter key, then clear the screen before exiting."""
    try:
        input("\nPress Enter to exit...")
    except EOFError:
        pass
    clear_screen()


def choose_base() -> float | None:
    """Prompt the user to choose a base and return it as float.

    Returns None if user input is invalid.
    """
    print("Choose base:")
    print("  1) natural (e)")
    print("  2) base 10")
    print("  3) custom base")
    try:
        choice = input("Enter choice (1/2/3): ").strip()
    except EOFError:
        return None

    if choice == "1":
        return math.e
    if choice == "2":
        return 10.0
    if choice == "3":
        try:
            b = float(input("Enter custom base (positive, not 1): ").strip())
        except (ValueError, EOFError):
            return None
        return b

    return None


def main() -> None:
    """Main loop: compute logarithms with user-selected base."""
    while True:
        clear_screen()

        # Read the number to compute log for
        try:
            s = input("Enter a positive number: ").strip()
            num = float(s)
        except (ValueError, EOFError):
            print("Invalid input. Please enter a numeric value.")
            try:
                again = input("Calculate another? (y/n): ").strip().lower()
            except EOFError:
                again = "n"
            if again.startswith("y"):
                continue
            else:
                pause_and_clear()
                break

        if num <= 0:
            print("Logarithm undefined for zero or negative numbers.")
            try:
                again = input("Calculate another? (y/n): ").strip().lower()
            except EOFError:
                again = "n"
            if again.startswith("y"):
                continue
            else:
                pause_and_clear()
                break

        base = choose_base()
        if base is None:
            print("Invalid base selection.")
            try:
                again = input("Calculate another? (y/n): ").strip().lower()
            except EOFError:
                again = "n"
            if again.startswith("y"):
                continue
            else:
                pause_and_clear()
                break

        # Validate base constraints
        if base <= 0 or abs(base - 1.0) < 1e-12:
            print("Base must be positive and not equal to 1.")
            try:
                again = input("Calculate another? (y/n): ").strip().lower()
            except EOFError:
                again = "n"
            if again.startswith("y"):
                continue
            else:
                pause_and_clear()
                break

        # Compute logarithm. math.log supports an optional base argument.
        try:
            result = math.log(num, base)
        except ValueError:
            # Fallback: compute via change of base if math.log raises
            result = math.log(num) / math.log(base)

        print(f"log base {base} of {num} = {result}")

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
    main()
