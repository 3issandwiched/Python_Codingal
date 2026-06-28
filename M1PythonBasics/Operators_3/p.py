def ascii_checker():
    print("=== Welcome to the ASCII Value Checker ===")
    print("Type 'exit' to quit the program.\n")
    
    while True:
        # Get input from the user
        user_input = input("Enter a single character (or text): ")
        
        # Check if the user wants to quit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        # Handle empty input
        if not user_input:
            print("You didn't enter anything! Please try again.\n")
            continue
            
        # Process single characters
        if len(user_input) == 1:
            # ord() converts a character to its ASCII/Unicode number
            ascii_code = ord(user_input)
            print(f"Character: '{user_input}' -> ASCII Value: {ascii_code}\n")
            
        # Process strings of text (Bonus feature!)
        else:
            print(f"Analyzing text sequence: '{user_input}'")
            for char in user_input:
                print(f"  '{char}' -> ASCII Value: {ord(char)}")
            print() # Print an empty line for spacing

# Run the program
if __name__ == "__main__":
    ascii_checker()
