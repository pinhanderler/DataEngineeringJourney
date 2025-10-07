# Project 2: Age Check 

age = int(input("Enter your age: "))

if age < 18:
    print("You are not an adult.")
else:
    print("You are an adult.")

birth_year = int(input("Enter your birth year: "))
calculated_age = 2025 - birth_year
print("Your age in 2025 is:", calculated_age)
