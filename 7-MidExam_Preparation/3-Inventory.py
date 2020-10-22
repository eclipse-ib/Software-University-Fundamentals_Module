collecting_items = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break

    splt_command = command.split(" - ")
    first_command = splt_command[0]
    item = splt_command[1]

    if first_command == "Collect":
        if item not in collecting_items:
            collecting_items.append(item)

    elif first_command == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)

    elif first_command == "Combine Items":
        items_split = item.split(":")
        old_item = items_split[0]
        new_item = items_split[1]
        if old_item in collecting_items:
            index_old_item = collecting_items.index(old_item)
            collecting_items.insert(index_old_item+1, new_item)

    elif first_command == "Renew":
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)

print(", ".join(collecting_items))
