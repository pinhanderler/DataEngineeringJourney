# Project 2: Age Check

print("Welcome to the Age Check Program!")

# Ask for age
age = int(input("Enter your age: "))

# Condition check
if age < 18:
    print("You are not an adult.")
else:
    print("You are an adult.")

# Ask for birth year and calculate age (based on 2025)
birth_year = int(input("Enter your birth year: "))
calculated_age = 2025 - birth_year

print(f"You are approximately {calculated_age} years old in 2025.")
