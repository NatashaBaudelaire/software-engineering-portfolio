n = int(input())

spider_ready = False
rhino_ready = False
spider_points = 0
rhino_points = 0

for _ in range(n):
    spider_phrase, rhino_phrase = input().strip(), input().strip()
    
    if spider_phrase == "Web Layer":
        spider_defence = True
    else:
        spider_defence = False
    
    if spider_phrase == "It's just a big mass of muscles":
        spider_ready = True
    elif spider_phrase == "Shoot web!":
        if spider_ready and not (rhino_phrase == "My muscles are solid!"):
            print("Damn insect!")
            spider_points += 1
        spider_ready = False

    if rhino_phrase == "My muscles are solid!":
        rhino_defence = True
    else:
        rhino_defence = False
    
    if rhino_phrase == "Now you'll see!":
        rhino_ready = True
    elif rhino_phrase == "Take this":
        if rhino_ready and not (spider_phrase == "Web Layer"):
            print("Drat, I slipped up")
            rhino_points += 1
        rhino_ready = False

if spider_points > rhino_points:
    print("You lost, big guy!")
elif rhino_points > spider_points:
    print("Ah well, just another ordinary day")
else:
    print("This isn’t working out")
