import math

def factorisation(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

num_lines = int(input("Enter the number of lines: "))

decomposition = []
min_length = 1000000000
chosen_line = 0

for i in range(num_lines):
    F = int(input(f"Enter number for line {i + 1}: "))
    temp_factors = factorisation(F)
    if len(temp_factors) < min_length:
        min_length = len(temp_factors)
        decomposition = temp_factors
        chosen_line = i
print(f"We will go with line {chosen_line + 1}")

if decomposition:
    unique_factors = sorted(list(set(decomposition)))
    for f in unique_factors:
        print(decomposition.count(f))
