decimal_num = int(input("Enter a decimal number: "))

# Handle 0 right away
if decimal_num == 0:
    binary_str = "0"
else:
    binary_str = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_str = str(remainder) + binary_str  # Puts the new digit at the front
        decimal_num //= 2  # Divides the number by 2 and drops the remainder

print(f"The binary representation is: {binary_str}")