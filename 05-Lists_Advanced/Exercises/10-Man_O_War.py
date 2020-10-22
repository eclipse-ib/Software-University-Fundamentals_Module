pirate_ship_status = [int(i) for i in input().split('>')]
warship_status = [int(i) for i in input().split('>')]
health_capacity = int(input())

while True:
    command_nosplit = input()
    if command_nosplit == "Retire":
        break
    command = command_nosplit.split()
    if "Fire" in command:
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index <= len(warship_status)-1:
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                exit()
        else:
            continue
    elif "Defend" in command:
        first_index = int(command[1])
        last_index = int(command[2])
        damage = int(command[3])
        if (0 <= first_index and first_index < last_index) and (last_index <= len(pirate_ship_status)-1):
            for i in range(first_index,last_index+1):
                pirate_ship_status[i] -= damage
                if pirate_ship_status[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    exit()
        else:
            continue
    elif "Repair" in command:
        index = int(command[1])
        repair = int(command[2])
        if 0 <= index <= len(pirate_ship_status)-1:
            pirate_ship_status[index] += repair
            if pirate_ship_status[index] > health_capacity:
                pirate_ship_status[index] = health_capacity
        else:
            continue
    elif "Status" in command:
        value_need_repair = health_capacity // 5
        sections_for_repair = 0
        for section in pirate_ship_status:
            if section < value_need_repair:
                sections_for_repair += 1
        print(f"{sections_for_repair} sections need repair.")
print(f"Pirate ship status: {sum(pirate_ship_status)}\nWarship status: {sum(warship_status)}")