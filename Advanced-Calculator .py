history_file = "history.txt"

# Show history
def show_history():
    try:
        with open(history_file, 'r') as file:
            lines = file.readlines()
        if len(lines) == 0:
            print("No history found here!...")
        else:
            print("\n--- Calculation History ---")
            for line in reversed(lines):#loops over the lines in reverse order (so the most recent line is printed first).
                print(line.strip())#prints each line after strip() removes leading/trailing whitespace and the newline.
            print("-------------------------\n")
    except FileNotFoundError:
        print("No history file found yet.")


# Clear history
# Your snippet (note: it has extra text after the print which will cause a syntax error)
def clear_history():
    file = open(history_file, "w")#Opening with "w" permanently erases the previous contents (unless you backed them up).
    file.close()
    print("History Cleared.")


# Save history
def save_history(equation, result):
    with open(history_file, 'a') as file:# if the file exists, new text will be added to the end; if it does not exist, Python creates the file.
        file.write(equation + " = " + str(result) + "\n")


# Calculation (now supports multiple operations)
def calculation(user_input):
    try:# Remove spaces → "5 + 6" → "5+6"
        user_input = user_input.replace(" ", "")  # remove spaces

         # Check invalid starting operator
        # if user_input[0] in "+*/%":
        #     print("Invalid input! Expression cannot start with an operator (except '-').")
        #     return
        
        # Block consecutive operators (like 2++3, 4--5, 5*-3, etc.)
        operators = '+-*/%'
        prev_char = ''
        for ch in user_input:
            if ch in operators and prev_char in operators:
                print("Invalid input! Expression has consecutive operators.")
                return
            prev_char = ch# Update prev_char to current character

        # Evaluate the expression
        result = eval(user_input)  # Python evaluates the math expression

        # Convert result to int if it's whole number
        if isinstance(result, float) and result.is_integer():#(4.5).is_integer()   # False (has decimal .5) AND (4.0).is_integer()   # True (no decimal .0)
            result = int(result)

        print("Result:", result)
        save_history(user_input, result)#Call your function that appends this expression + result to the history file.

    except ZeroDivisionError:
        print("Error: Division by zero not allowed.")
    except Exception:
        print("Invalid input! Please enter a valid math expression.")

# Main loop
def main():
    print("Welcome to the Calculator!")
    while True:
        user_input = input("Enter calculation (+,-,*,/,%) or command (history, clear, exit): ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculation(user_input)

main()
