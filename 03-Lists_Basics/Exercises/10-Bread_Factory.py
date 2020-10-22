working_events = input().split("|")
energy = 100
coins = 100

for i in working_events:
    event = i.split("-")
    if event[0] == "rest":
        if energy + int(event[1]) > 100:
            gained_energy = 100 - energy
            print(f"You gained {gained_energy} energy.")
            energy = 100
        else:
            energy += int(event[1])
            print(f"You gained {int(event[1])} energy.")
        print(f"Current energy: {energy}.")
    elif event[0] == "order":
        if energy >= 30:
            energy -= 30
            print(f"You earned {int(event[1])} coins.")
            coins += int(event[1])
        else:
            energy += 50
            print(f"You had to rest!")
            continue
    else:
        if int(event[1]) < coins:
            coins -= int(event[1])
            print(f"You bought {event[0]}.")
        else:
            print(f"Closed! Cannot afford {event[0]}.")
            exit()
print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")