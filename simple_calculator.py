def perform_operation(num1, num2, operation):
    """Performs the specified mathematical operation on num1 and num2."""
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is undefined."
        result = num1 / num2
    else:
        return "Error: Invalid operation."
    return result

# Ask the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
result = perform_operation(num1, num2, operation)

# Print the result
if isinstance(result, str):
    print(result)
else:
    print(f"{num1} {operation} {num2} = {result}")