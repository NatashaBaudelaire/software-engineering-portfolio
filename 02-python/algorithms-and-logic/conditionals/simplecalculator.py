n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ").strip()

if operation == '+':
    result = n1 + n2
    print(f"You chose addition. The result is {result:.2f}")
elif operation == '-':
    result = n1 - n2
    print(f"You chose subtraction. The result is {result:.2f}")
elif operation == '*':
    result = n1 * n2
    print(f"You chose multiplication. The result is {result:.2f}")
elif operation == '/':
    if n2 != 0:
        result = n1 / n2
        print(f"You chose division. The result is {result:.2f}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose '+', '-', '*' or '/'.")
