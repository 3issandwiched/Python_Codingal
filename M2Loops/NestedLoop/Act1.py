# ATM Cash Dispenser
print("=== ATM Cash Dispenser ===")
print("Dispensing cash for customers one at a time.\n")
notes = [100, 50, 20, 10, 5, 1]

serving = True
while serving:

    name = input("Enter customer name: ")
    amount = int(input(f"Hello {name}! Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount. Please enter a positive number.\n")
        continue

    print(f"\nDispensing {amount} units for {name}:")
    print("-" * 30)

    remaining = amount  # copy
    i = 0
   
    # Inner while loop — breaks amount into notes
    while i < len(notes):
        count = remaining // notes[i]
        if count > 0:
            print(f"  {count}  x  {notes[i]}-unit note(s)  =  {count * notes[i]}")
           
            remaining -= count * notes[i]
        i += 1

    
    print(f"Transaction complete! Please collect your cash, {name}.\n")

    again = input("Next customer? (yes / no): ").strip().lower()
    if again != "yes":
        serving = False # break

