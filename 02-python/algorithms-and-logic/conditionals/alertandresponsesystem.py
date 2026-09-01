goal = int(input("Enter the target number of infiltrators: "))
infiltrators = int(input("Enter the initial number of infiltrators: "))

alert = 0

for _ in range(int(input("Enter number of events: "))):
    event = input("Enter event: ").split()
    event_type = event[0]
    
    if event_type == "Substitution":
        new_infiltrators = int(event[1])
        infiltrators += new_infiltrators
        
    elif event_type == "Counter-attack":
        detected = int(event[1])
        infiltrators -= detected
        
    elif event_type == "Exposure":
        alert += 30
        
    if alert >= 100:
        print("It's not worth continuing, let's retreat and devise a new plan...")
        break
    
    if infiltrators >= goal:
        print("Order an attack immediately, this time we will dominate the Earth!")
        break
    
    else:
        if infiltrators <= 0:
            print("We have completely failed, there are no more Skrull infiltrators!")
        elif alert < 100:
            print("It's not worth continuing, let's retreat and devise a new plan...")
        elif infiltrators < goal:
            print("We are still not ready to attack, let's wait a little longer...")
