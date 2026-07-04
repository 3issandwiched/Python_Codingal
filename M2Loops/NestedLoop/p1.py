def decimal_to_binary_math():
    try:
        decimal_num = int(input("Enter a decimal number: "))
        
        # Handle 0 as a special case
        if decimal_num == 0:
            print("The binary representation is: 0")
            return
            
        binary_digits = []
        temp = decimal_num
        
        # Keep dividing by 2 until we hit 0
        while temp > 0:
            remainder = temp % 2
            binary_digits.append(str(remainder))
            temp //= 2  # Integer division to move to the next step
            
        # The remainders are collected in reverse order, so we flip them
        binary_digits.reverse()
        binary_num = "".join(binary_digits)
        
        print(f"The binary representation of {decimal_num} is: {binary_num}")
        
    except ValueError:
        print("Please enter a valid whole number.")

# Run the program
decimal_to_binary_math()