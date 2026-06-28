# Take integer inputs from the user
a = int(input("Enter a value: "))
b = int(input("Enter value 2: "))
c = int(input("Enter value 3: "))

# Calculate the average (this will be a float decimal)
avg = (a + b + c) / 3
print(f"avg = {avg:.2f}")  # Formats average to 2 decimal places

# Track which variables are smaller than the average
higher_than = []

if avg > a:
    higher_than.append(f"a ({a})")
if avg > b:
    higher_than.append(f"b ({b})")
if avg > c:
    higher_than.append(f"c ({c})")

# Print the final result dynamically based on the conditions met
if len(higher_than) == 0:
    print("The average is equal to all inputs.")
else:
    # Joins the list items cleanly with commas
    comparison_text = ", ".join(higher_than)
    print(f"The average ({avg:.2f}) is higher than {comparison_text}")
