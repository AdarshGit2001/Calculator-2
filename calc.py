def calc(num1, num2, operation):
    if operation in ['add', '+']:
        return num1 + num2
    elif operation in ['subtract', '-']:
        return num1 - num2
    elif operation in ['multiply', '*']:
        return num1 * num2
    elif operation in ['divide', '/']:
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "Error: Invalid operation."

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, / or add, subtract...): ").lower()

        result = calc(num1, num2, op)
        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers!")
