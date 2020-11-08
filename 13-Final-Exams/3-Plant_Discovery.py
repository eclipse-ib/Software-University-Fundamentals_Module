number_of_plants = int(input())

plants = {}

for i in range(number_of_plants):
    new_plant_command = input().split("<->")
    name = new_plant_command[0]
    rarity = int(new_plant_command[1])
    if name not in plants:
        plants[name] = {}
        plants[name]["rarity"] = rarity
    else:
        plants[name]["rarity"] = rarity

while True:
    commands = input().split(": ")
    if "Exhibition" in commands[0]:
        break

    command = commands[0]

    if command == "Rate":
        rate_name, rating = commands[1].split(" - ")
        if rate_name in plants:
            if "rating" not in plants[rate_name]:
                plants[rate_name]["rating"] = [int(rating)]
            else:
                plants[rate_name]["rating"] += [int(rating)]
        else:
            print("error")

    elif command == "Update":
        update_name, new_rarity = commands[1].split(" - ")
        if update_name in plants:
            if "rarity" not in plants[update_name]:
                plants[update_name]["rarity"] = int(new_rarity)
            else:
                plants[update_name]["rarity"] = int(new_rarity)
        else:
            print("error")

    elif command == "Reset":
        reset_name = commands[1]
        if reset_name in plants:
            plants[reset_name]["rating"] = []
        else:
            print("error")

    else:
        print("error")

print(f"Plants for the exhibition:")

for k, v in plants.items():
    if v['rating'] != []:
        plants[k]['rating'] = sum(v['rating']) / len(v['rating'])
    else:
        v['rating'] = 0

sorted_plants = sorted(plants.keys(), key=lambda p: (-plants[p]["rarity"], -plants[p]["rating"]))
for k in sorted_plants:
    print(f"- {k}; Rarity: {plants[k]['rarity']}; Rating: {plants[k]['rating']:.2f}")