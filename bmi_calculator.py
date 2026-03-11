# Python Program to Calculate Body Mass Index (BMI)

# BMI is a measure of body fat based on weight and height.
# Formula: BMI = weight (kg) / height (m) ^ 2
# WHO Classification:
#   BMI < 18.5           → Underweight
#   18.5 <= BMI < 25.0   → Normal weight
#   25.0 <= BMI < 30.0   → Overweight
#   BMI >= 30.0          → Obese
#
# Note: BMI is gender-neutral, but healthy body fat percentage
# differs between males and females. This program provides
# gender- and age-aware interpretations alongside the standard result.

import os

# Keep the program running until the user decides to exit
while True:
    # Clear the console screen for a clean display on each iteration
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # --- Collect user inputs ---

        # Take weight input in kilograms and convert to float
        weight = float(input("Enter your weight in kilograms (kg): "))

        # Take height input in meters and convert to float
        height = float(input("Enter your height in meters (m): "))

        # Take age input and convert to integer
        age = int(input("Enter your age (years): "))

        # Take gender input and normalise to lowercase
        # Accepts full words (male/female) or shorthand (m/f)
        gender = input("Enter your gender (m/f): ").strip().lower()

        # Normalise shorthand to full word for consistent downstream checks
        if gender == 'm':
            gender = 'male'
        elif gender == 'f':
            gender = 'female'

        # Validate gender input
        if gender not in ['male', 'female']:
            print("Invalid gender! Please enter 'm' or 'f' (or 'male' / 'female').")

        # Validate that weight, height, and age are positive numbers
        elif weight <= 0 or height <= 0 or age <= 0:
            print("Invalid input! Weight, height, and age must be positive values.")

        else:
            # --- Calculate BMI ---
            # Standard formula: BMI = weight(kg) / height(m)^2
            bmi = weight / (height ** 2)

            # Display BMI rounded to 2 decimal places
            print(f"\nYour BMI is: {bmi:.2f}")

            # --- WHO Standard BMI Classification (applies to all adults) ---
            print("\n--- WHO BMI Classification ---")
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25.0:
                category = "Normal weight"
            elif 25.0 <= bmi < 30.0:
                category = "Overweight"
            else:
                # BMI >= 30.0
                category = "Obese"
            print(f"Category: {category}")

            # --- Gender-aware body fat interpretation ---
            # Healthy body fat % ranges differ between males and females:
            #   Males  : Essential 2-5%, Athletes 6-13%, Fit 14-17%, Acceptable 18-24%, Obese 25%+
            #   Females: Essential 10-13%, Athletes 14-20%, Fit 21-24%, Acceptable 25-31%, Obese 32%+
            print("\n--- Gender-Aware Interpretation ---")
            if gender == 'male':
                if bmi < 18.5:
                    print("For males: You may have low muscle mass or insufficient caloric intake.")
                elif 18.5 <= bmi < 25.0:
                    print("For males: You are in a healthy range. Typical healthy body fat is 14–24%.")
                elif 25.0 <= bmi < 30.0:
                    print("For males: You are overweight. Consider balanced diet and regular exercise.")
                    print("           Note: Muscular males may show higher BMI without excess body fat.")
                else:
                    print("For males: High obesity risk. A healthcare consultation is recommended.")

            else:  # female
                if bmi < 18.5:
                    print("For females: You may have low body fat; risk of hormonal and bone issues.")
                elif 18.5 <= bmi < 25.0:
                    print("For females: You are in a healthy range. Typical healthy body fat is 21–31%.")
                elif 25.0 <= bmi < 30.0:
                    print("For females: You are overweight. Healthy lifestyle changes are advisable.")
                else:
                    print("For females: High obesity risk. A healthcare consultation is recommended.")

            # --- Age-aware note ---
            # BMI thresholds apply to adults (age 18+).
            # For children and teens, BMI is interpreted using age- and sex-specific percentiles.
            print("\n--- Age Note ---")
            if age < 18:
                print(f"Note: You are {age} years old. Standard BMI categories are designed for adults (18+).")
                print("      For children and teens, BMI should be assessed using age- and gender-specific")
                print("      growth charts. Please consult a pediatrician for an accurate evaluation.")
            elif age >= 65:
                print(f"Note: You are {age} years old. For older adults (65+), a slightly higher BMI")
                print("      (up to ~27) may be protective. Consult your doctor for personalised advice.")
            else:
                print(f"Note: Standard adult BMI categories apply to your age ({age}).")

    except ValueError:
        # Handle non-numeric input gracefully
        print("Invalid input! Please enter valid numeric values for weight, height, and age.")

    # Ask the user if they want to perform another calculation
    choice = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for using the BMI Calculator!")
        break
