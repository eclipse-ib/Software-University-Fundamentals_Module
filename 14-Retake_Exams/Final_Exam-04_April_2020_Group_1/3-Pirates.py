cities = {}

while True:
    cities_command = input().split("||")
    if cities_command[0] == "Sail":
        break

    city = cities_command[0]
    population = int(cities_command[1])
    gold = int(cities_command[2])

    if city not in cities:
        cities[city] = {}
        cities[city]["population"] = population
        cities[city]["gold"] = gold
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

while True:
    events = input().split("=>")
    if events[0] == "End":
        break

    command = events[0]
    town = events[1]

    if command == "Plunder":
        if town in cities:
            people = int(events[2])
            plunder_gold = int(events[3])
            cities[town]["population"] -= people

            if cities[town]["population"] <= 0:
                print(f"{town} plundered! {plunder_gold} gold stolen, {people} citizens killed.")
                print(f"{town} has been wiped off the map!")
                del cities[town]
                continue

            cities[town]["gold"] -= plunder_gold
            if cities[town]["gold"] <= 0:
                print(f"{town} plundered! {plunder_gold} gold stolen, {people} citizens killed.")
                print(f"{town} has been wiped off the map!")
                del cities[town]
                continue

            print(f"{town} plundered! {plunder_gold} gold stolen, {people} citizens killed.")

        else:
            continue

    if command == "Prosper":
        prosper_gold = int(events[2])
        if prosper_gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue

        cities[town]["gold"] += prosper_gold
        print(f"{prosper_gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
if len(cities) != 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")

    sorted_cities = sorted(cities.keys(), key=lambda c: (-cities[c]["gold"], c))
    for city in sorted_cities:
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")

else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")