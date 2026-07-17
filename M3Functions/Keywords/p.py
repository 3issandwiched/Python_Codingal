def calculate_due_amount(total_bill, amount_paid):
    """
    Calculates the remaining due amount.
    Returns 0 if the bill is fully paid or overpaid.
    """
    if amount_paid >= total_bill:
        return 0.0
    else:
        return total_bill - amount_paid

# Example usage:
bill = float(input("Enter total bill amount: "))
paid = float(input("Enter amount paid by customer: "))

due = calculate_due_amount(bill, paid)

if due > 0:
    print(f"The remaining due amount is: ${due:.2f}")
else:
    print("The bill is fully paid. No amount due.")