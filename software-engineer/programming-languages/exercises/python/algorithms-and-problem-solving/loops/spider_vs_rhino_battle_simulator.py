spider_actions = {
    "Layer of webs": "D",
    "Just a big mass of muscles": "P",
    "Shoot web!": "A"
}

rhino_actions = {
    "My muscles are solid!": "D",
    "Now you'll see!": "P",
    "Take this": "A"
}

rounds = int(input("Enter number of rounds: "))

spider_ready = False
rhino_ready = False
spider_points = 0
rhino_points = 0

print("\nLet the battle begin!\n")

for i in range(1, rounds + 1):
    print(f"--- Round {i} ---")
    spider_phrase = input("Spider says: ").strip()
    rhino_phrase = input("Rhino says: ").strip()

    spider_action = spider_actions.get(spider_phrase)
    rhino_action = rhino_actions.get(rhino_phrase)

    if not spider_action or not rhino_action:
        print("Invalid phrase detected! Skipping round.\n")
        continue
    if spider_action == "A":
        if spider_ready and rhino_action != "D":
            spider_points += 1
            print("Spider strikes! Rhino takes a hit!")
        else:
            print("Spider attacks, but Rhino dodges or Spider was unprepared.")
        spider_ready = False
    elif spider_action == "P":
        spider_ready = True
        print("Spider is preparing a move...")
    if rhino_action == "A":
        if rhino_ready and spider_action != "D":
            rhino_points += 1
            print("Rhino charges! Spider takes a hit!")
        else:
            print("Rhino attacks, but Spider dodges or Rhino was unprepared.")
        rhino_ready = False
    elif rhino_action == "P":
        rhino_ready = True
        print("Rhino is flexing muscles and preparing a move...")
    print(f"Score: Spider {spider_points} - Rhino {rhino_points}\n")

print("--- Battle Result ---")
if spider_points > rhino_points:
    print("Spider wins! Rhino defeated!")
elif rhino_points > spider_points:
    print("Rhino wins! Spider retreats!")
else:
    print("It's a tie! The battle ends inconclusively.")
