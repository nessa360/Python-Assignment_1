# Simple Calculator Program

This is a simple Python program that allows users to perform basic mathematical operations (addition, subtraction, multiplication, and division).

## Features

- Takes two numbers and a mathematical operation from the user.
- Performs the specified operation.
- Displays the result or an appropriate error message.

## Dependencies

- Python 3.x

## How to Run

1. **Save the file**: Save the Python script as `simple_calculator.py` in your desired directory.
2. **Open Terminal**: Open a terminal or command prompt.
3. **Navigate to the directory**: Use `cd` command to navigate to the directory where your script is saved.
4. **Run the script**: Type `python simple_calculator.py` and press Enter.

## Usage

When you run the script, you will be prompted to enter:

- The first number.
- The second number.
- The operation you want to perform (`+`, `-`, `*`, or `/`).

### Example

```sh
Enter the first number: 10
Enter the second number: 5
Enter the operation (+, -, *, /): +
10 + 5 = 15

Error Handling
If you try to divide by zero, the program will display an error message.
If you enter an invalid operation, the program will display an error message.
Enter the first number: 10
Enter the second number: 0
Enter the operation (+, -, *, /): /
Error: Division by zero is undefined.