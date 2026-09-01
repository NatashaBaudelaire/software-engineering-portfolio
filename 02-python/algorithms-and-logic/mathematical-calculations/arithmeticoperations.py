def factorial(n):
    if n < 0:
        return 0
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

K = int(input("Enter the number of operations: ").strip())
RESPONSE = None

for _ in range(K):
    data = input("Enter operation: ").split()
    
    if data[0] == "RESPONSE":
        A = RESPONSE
    else:
        A = int(data[0])
    
    op = data[1]
    
    if data[2] == "RESPONSE":
        B = RESPONSE
    else:
        B = int(data[2])
    
    if op == "@":
        result = factorial(A + B) // (factorial(A) * factorial(B)) * A * B
    elif op == "?":
        result = factorial(A + B) // factorial(B)
    elif op == ">":
        result = factorial(A) * factorial(B)
    elif op == "<":
        result = factorial(A + B) - factorial(A) - factorial(B)
    elif op == "+":
        result = A + B
    elif op == "-":
        result = A - B
    elif op == "*":
        result = A * B
    elif op == "/":
        result = A // B if B != 0 else 0
    else:
        result = 0
    
    print(result)
    RESPONSE = result
