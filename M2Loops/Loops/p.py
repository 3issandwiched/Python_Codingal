def calculate_power_loop(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Example usage:
print(calculate_power_loop(5, 3)) 
# Output: 125