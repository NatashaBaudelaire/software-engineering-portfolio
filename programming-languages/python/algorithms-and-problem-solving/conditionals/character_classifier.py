character = input().strip()

if character in "+-*/":
    print("The character is a mathematical operation")

elif character.isnumeric():
    print("The character is a number")

elif character.lower() in "aeiou":
    print("The character is a vowel")
