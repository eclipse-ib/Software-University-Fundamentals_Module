groceries = input().split("!")

while True:
    command_no_splt = input()
    if command_no_splt == "Go Shopping!":
        break
    command = command_no_splt.split()
    main_command = command[0]
    item = command[1]

    if main_command == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)
        else:
            continue

    elif main_command == "Unnecessary":
        if item in groceries:
            groceries.remove(item)
        else:
            continue

    elif main_command == "Correct":
        if item in groceries:
            old_name = groceries.index(item)
            new_item = command[2]
            groceries[old_name] = new_item
        else:
            continue

    elif main_command == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

print(", ".join(groceries))