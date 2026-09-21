X = int(input("Enter the number of students: "))

names = []
powers = []

for _ in range(X):
    entry = input("Enter name and power: ").split()
    name = entry[0]
    power = int(entry[1])
    names.append(name)
    powers.append(power)

highest_power = powers[0]
lowest_power = powers[0]

for power in powers:
    if power > highest_power:
        highest_power = power
    if power < lowest_power:
        lowest_power = power

strongest = []
weakest = []

for i in range(X):
    if powers[i] == highest_power:
        strongest.append(names[i])
    if powers[i] == lowest_power:
        weakest.append(names[i])

print(f"Mr. Dumbledore, the highest magic power was {highest_power}, and the new team will consist of the following student(s): {', '.join(strongest)}. Unfortunately, the lowest power level was {lowest_power} and the student(s) expelled: {', '.join(weakest)}.")