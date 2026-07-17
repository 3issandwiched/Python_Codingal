def check_age(age):
    # Check if age is a valid number (e.g., between 0 and 120)
    if age < 0 or age > 120:
        print("Error: Please enter a valid age between 0 and 120.")
    else:
        # Check if age is even or odd using the modulo operator
        if age % 2 == 0:
            print(f"Age {age} is valid and it is an even number.")
        else:
            print(f"Age {age} is valid and it is an odd number.")

# Get input from the user
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError:
    print("Error: Please enter a whole number for your age.")