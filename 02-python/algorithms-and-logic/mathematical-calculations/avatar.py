import math

valid_avatars = [
    "Korra of the Southern Water Tribe",
    "Aang of the Southern Air Temple",
    "Roku of the Fire Nation",
    "Kyoshi of the Earth Kingdom",
    "Kuruk of the Northern Water Tribe",
    "Yangchen of the Western Air Temple",
    "Szeto of the Fire Nation",
    "Wan the First"
]

count = {avatar: 0 for avatar in valid_avatars}

while True:
    try:
        name = input().strip()
        if name in count:
            count[name] += 1
    except EOFError:
        break
max_occurrences = max(count.values())

if max_occurrences == 0:
    print("No Avatar was found")
else:
    avatars_max = [name for name, qty in count.items() if qty == max_occurrences]

    if all(qty == max_occurrences for qty in count.values()):
        print("You found all the Avatars")
    elif len(avatars_max) == 1:
        print(f"The Avatar you found was {avatars_max[0]}")
    else:
        print(f"You found {len(avatars_max)} Avatars, and they were:")
        for name in avatars_max:
            print(name)