def calculate_square(number):
    return number ** 2

def print_result(result):
    print("The square of the number is:", result)

number = int(input("Enter any number: "))
square = calculate_square(number)
print_result(square)