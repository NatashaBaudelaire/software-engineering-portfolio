def add(n1, n2):
    """Add two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Subtract second number from first."""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Divide first number by second."""
    if n2 != 0:
        return n1 / n2
    else:
        return None

def get_numbers():
    """Get two numbers from user input."""
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    return n1, n2

def get_operation():
    """Get operation choice from user."""
    return input("Enter the operation (+, -, *, /): ").strip()

def calculate(n1, n2, operation):
    """Perform calculation based on operation."""
    if operation == '+':
        return add(n1, n2), "addition"
    elif operation == '-':
        return subtract(n1, n2), "subtraction"
    elif operation == '*':
        return multiply(n1, n2), "multiplication"
    elif operation == '/':
        result = divide(n1, n2)
        if result is not None:
            return result, "division"
        else:
            return None, "division"
    else:
        return None, None

def display_result(result, operation_name):
    """Display the calculation result."""
    if result is not None:
        print(f"You chose {operation_name}. The result is {result:.2f}")
    elif operation_name == "division":
        print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose '+', '-', '*' or '/'.")

def main():
    """Main calculator function."""
    n1, n2 = get_numbers()
    operation = get_operation()
    result, operation_name = calculate(n1, n2, operation)
    display_result(result, operation_name)

if __name__ == "__main__":
    main()
