#Task: Calculator Program
#   Create a Python program that acts as a basic calculator. It should prompt the user to
#   enter two numbers and an operator (+ - *  / %), and then display the result of the operation.

def calculator():
    while True:
        try:
            num1_input = input("Enter the first number: ")
            num1 = float(num1_input)
            break
        except ValueError:
            print(f"'{num1_input}' is not a valid number.")

    valid_operators = ['+', '-', '*', '/', '%']
    while True:
        operator = input(f"Enter an operator ({', '.join(valid_operators)}): ")
        if operator in valid_operators:
            break 
        else:
            print(f"'{operator}' is not a valid operator.")

    while True:
        try:
            num2_input = input("Enter the second number: ")
            num2 = float(num2_input)
            if operator in ('/', '%') and num2 == 0:
                print("Error: Cannot divide or modulous by zero.")
                continue
            break
        except ValueError:
            print(f"'{num2_input}' is not a valid number.")
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2

    print("\n--- Result ---")
    print(f"{num1:g} {operator} {num2:g} = {result:g}")

if __name__ == "__main__":
    calculator()