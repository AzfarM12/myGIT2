# Simple Calculator

# Input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Choose operation
operation = input("Choose operation (+, -, *, /): ")

# Calculate
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error (division by zero)"
else:
    result = "Invalid operation"

# Output
print("Result:", result)