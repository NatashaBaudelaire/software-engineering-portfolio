num_opponents = int(input("Enter number of opponents: "))
average_health = int(input("Enter average health: "))

all_defeated = True

for _ in range(num_opponents):
    name = input("Enter opponent name: ").strip()
    health = int(input("Enter opponent health: "))
    attacks = int(input("Enter number of attacks: "))
    
    total_damage = 0
    for _ in range(attacks):
        total_damage += int(input("Enter damage: "))
    if health < 0.5 * average_health:
        planet = "Asgard"
    elif 0.5 * average_health <= health <= 0.8 * average_health:
        planet = "Xandar"
    elif 0.8 * average_health < health < 1.2 * average_health:
        planet = "Sakaar"
    elif 1.2 * average_health <= health <= 1.5 * average_health:
        planet = "Vormir"
    else:
        planet = "Ego"
    
    if total_damage >= health:
        print(f"{name} from planet {planet} was defeated!")
    else:
        print(f"{name}, from planet {planet}, managed to escape.")
        all_defeated = False
if all_defeated:
    print("We managed to keep the galaxy safe.")
else:
    print("Some opponents are still lurking...")
