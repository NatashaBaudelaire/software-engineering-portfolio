ranking = [input("Enter player name: ").strip() for _ in range(14)]
initial_champion = ranking[0]
N = int(input("Enter number of events: ").strip())

for _ in range(N):
    data = input("Enter event: ").split()
    name = data[0]
    action = data[1]
    pos = ranking.index(name)
    
    if action in ["captured", "recovered"]:
        if pos > 0:
            ranking[pos], ranking[pos-1] = ranking[pos-1], ranking[pos]
    elif action in ["fell", "foul"]:
        if pos < 13:
            ranking[pos], ranking[pos+1] = ranking[pos+1], ranking[pos]

first = ranking[0]
last = ranking[13]

if first == initial_champion:
    print(f"The wizard {first} was exemplary during the match and showed everyone that Quidditch is more than just a sport. Meanwhile, the wizard {last} was unable to perform well and will be relegated to the second division of wizards.")
else:
    print(f"It was an extremely intense match and the wizard {first} proved superior and claimed first place, while the wizard {last} performed poorly and will be relegated to the second division of wizards.")
