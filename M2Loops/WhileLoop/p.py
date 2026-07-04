def count_digits_math():
    try:
        # Convert input to an integer
        number = int(input("Enter a whole number: "))
        
        # Handle 0 specifically, since the loop won't run for 0
        if number == 0:
            print("The number of digits is: 1")
            return
            
        # Make the number positive so the math works perfectly
        temp = abs(number)
        count = 0
        
        while temp > 0:
            temp //= 10  # Floor division: cuts off the last digit (e.g., 123 becomes 12)
            count += 1
            
        print(f"The number of digits is: {count}")
        
    except ValueError:
        print("Please enter a valid whole number.")

# Run the function
count_digits_math()