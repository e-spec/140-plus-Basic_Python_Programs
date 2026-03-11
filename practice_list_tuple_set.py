# Python program to practice with list, tuple, and set

# Import required module for clearing terminal screen
import os


# Parse comma-separated numbers from user input
def parse_numbers(user_input):
    """Convert comma-separated input into a list of integers."""
    return [int(item.strip()) for item in user_input.split(',') if item.strip()]


# Practice common list operations
def list_practice():
    print("\n=== List Practice ===")
    # Create a list from user input
    items = parse_numbers(input("Enter numbers separated by commas: "))
    print(f"Original list: {items}")

    # Add an element to the list
    items.append(100)
    print("Method: items.append(100)")
    print(f"Result: {items}")
    print()

    # Insert an element at a specific position
    items.insert(1, 50)
    print("Method: items.insert(1, 50)")
    print(f"Result: {items}")
    print()

    # Extend the list with multiple elements
    items.extend([200, 300])
    print("Method: items.extend([200, 300])")
    print(f"Result: {items}")
    print()

    # Sort list in ascending order
    items.sort()
    print("Method: items.sort()")
    print(f"Result: {items}")
    print()

    # Count occurrences of a value
    print("Method: items.count(100)")
    print(f"Result: Count of 100: {items.count(100)}")
    print()

    # Find index of a value if present
    if 100 in items:
        print("Method: items.index(100)")
        print(f"Result: Index of 100: {items.index(100)}")
        print()

    # Remove first occurrence of a value if present
    if 50 in items:
        items.remove(50)
        print("Method: items.remove(50)")
        print(f"Result: {items}")
        print()

    # Reverse list order
    items.reverse()
    print("Method: items.reverse()")
    print(f"Result: {items}")
    print()

    # Remove and show last element (if list is not empty)
    if items:
        removed = items.pop()
        print("Method: items.pop()")
        print(f"Result: Removed {removed}, List: {items}")
        print()



# Practice common tuple operations
def tuple_practice():
    print("\n=== Tuple Practice ===")
    # Create a tuple from user input
    items = tuple(parse_numbers(input("Enter numbers separated by commas: ")))
    print(f"Tuple: {items}")

    # Show tuple length and simple tuple queries
    print(f"Length: {len(items)}")
    if items:
        print(f"First element: {items[0]}")
        print(f"Count of first element: {items.count(items[0])}")



# Practice common set operations
def set_practice():
    print("\n=== Set Practice ===")
    # Create two sets from user input
    first = set(parse_numbers(input("Enter first set (comma-separated numbers): ")))
    second = set(parse_numbers(input("Enter second set (comma-separated numbers): ")))

    # Show results of set operations
    print(f"Set A: {first}")
    print(f"Set B: {second}")
    print(f"Union (A | B): {first | second}")
    print(f"Intersection (A & B): {first & second}")
    print(f"Difference (A - B): {first - second}")


# Main program entry point
if __name__ == "__main__":
    # Clear terminal for a clean interface
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display menu options
    print("=== Practice Program: List, Tuple, Set ===")
    print("1. Practice List")
    print("2. Practice Tuple")
    print("3. Practice Set")

    # Get user menu choice and keep asking until it's valid
    choice = input("\nChoose an option (1, 2, or 3): ")
    while choice not in ('1', '2', '3'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Practice Program: List, Tuple, Set ===")
        print("1. Practice List")
        print("2. Practice Tuple")
        print("3. Practice Set")
        print("Invalid choice! Please enter a correct option (1, 2, or 3).")
        choice = input("Choose an option (1, 2, or 3): ")

    # Run selected practice block and handle invalid numeric input
    try:
        if choice == '1':
            list_practice()
        elif choice == '2':
            tuple_practice()
        elif choice == '3':
            set_practice()
    except ValueError:
        print("Invalid input! Please enter only numbers separated by commas.")
