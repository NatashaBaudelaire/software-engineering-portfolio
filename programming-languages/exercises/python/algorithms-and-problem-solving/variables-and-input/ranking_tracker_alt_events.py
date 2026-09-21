# Alternative event vocabulary: caught/recovered rank a wizard up, fell/penalty rank a wizard down
ranking = [input("Enter player name: ").strip() for _ in range(14)]
initial_champion = ranking[0]


N = int(input("Enter number of events: ").strip())

for _ in range(N):
    data = input("Enter action: ").split()
    name = data[0]
    action = data[1]
    pos = ranking.index(name)


    if action in ["caught", "recovered"]:
        if pos > 0:
            ranking[pos], ranking[pos - 1] = ranking[pos - 1], ranking[pos]
    elif action in ["fell", "penalty"]:
        if pos < 13:
            ranking[pos], ranking[pos + 1] = ranking[pos + 1], ranking[pos]


first = ranking[0]
last = ranking[13]


if first == initial_champion:
    print(f"The wizard {first} played exemplary during the match and showed everyone that Quidditch is more than a sport. However, the wizard {last} performed poorly and will be relegated to the second division of wizards.")
else:
    print(f"The match was extremely intense. The wizard {first} demonstrated superiority and conquered first place, whereas the wizard {last} played terribly and will be relegated to the second division of wizards.")
