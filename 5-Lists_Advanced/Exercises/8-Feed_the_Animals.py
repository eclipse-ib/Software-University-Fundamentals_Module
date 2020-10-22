names_feed_limit = {}
areas = {}


while True:
    command_nosplt = input()
    if command_nosplt == "Last Info":
        break
    command = command_nosplt.split(":")
    if "Last" in command:
        break
    if "Add" in command:
        if command[1] in names_feed_limit.keys():
            names_feed_limit[command[1]] += int(command[2])
            continue
        else:
            names_feed_limit[command[1]] = int(command[2])
        if command[3] not in areas.keys():
            areas[command[3]] = 1
        else:
            areas[command[3]] += 1
    elif "Feed" in command:
        if command[1] in names_feed_limit.keys():
            names_feed_limit[command[1]] -= int(command[2])
            if names_feed_limit[command[1]] <= 0:
                print(f"{command[1]} was successfully fed")
                del names_feed_limit[command[1]]
                areas[command[3]] -= 1

sorted_value = sorted(names_feed_limit.items(), key=lambda item: item[1], reverse=True)
print(f"Animals:")
for name in sorted_value:
    print(f"{name[0]} -> {name[1]}g")

sorted_areas = sorted(areas.items(), key=lambda item: item[1], reverse=True)
print(f"Areas with hungry animals:")
for area in sorted_areas:
    if int(area[1]) > 0:
        print(f"{area[0]} : {area[1]}")