target = int(input("Enter the target amount: "))
num_medicines = int(input("Enter the number of medicines: "))

medicines = []
for _ in range(num_medicines):
    name, qty = input("Enter medicine name and quantity: ").split()
    medicines.append((name, int(qty)))
found = False

for start in range(num_medicines):
    total = 0
    sublist = []
    for name, qty in medicines[start:]:
        total += qty
        sublist.append(name)
        if total == target:
            print(f"We won the battle and humanity is restored! {' '.join(sublist)} were used to de-alligatorize")
            found = True
            break
    if found:
        break

if not found:
    print("I feel something strange... could I be the next alligator?")