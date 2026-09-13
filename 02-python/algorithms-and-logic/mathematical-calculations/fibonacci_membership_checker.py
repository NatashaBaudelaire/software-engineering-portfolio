import math

def is_perfect_square(n):

    root = int(math.isqrt(n))

    return root * root == n

def is_in_fibonacci_sequence(num):

    
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

entry = input().split(",")

numbers = [int(x.strip()) for x in entry]


belongs = [is_in_fibonacci_sequence(num) for num in numbers]

if all(belongs):
    print("Very good, Morty! Let's go on more adventures!")
elif not any(belongs):
    print("Oh my god, Morty! You really need to go to school!")
else:
    print("There's still room for improvement, Morty!")