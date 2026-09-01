first_name = input("Enter first name: ")
last_name = input("Enter surname: ")
age = int(input("Enter age: "))

full_name = first_name + " " + last_name

if age < 12:
    print(f"The athlete {full_name} belongs to the junior category.")
elif 12 <= age <= 17:
    print(f"The athlete {full_name} belongs to the youth category.")
elif 18 <= age <= 35:
    print(f"The athlete {full_name} belongs to the adult category.")
else:
    print(f"The athlete {full_name} belongs to the masters category.")
