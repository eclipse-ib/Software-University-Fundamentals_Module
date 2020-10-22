targets = [int(i) for i in input().split()]

while True:
    commands = input().split()
    if commands[0] == "End":
        targets = [str(i) for i in targets]
        print("|".join(targets))
        break
    command = commands[0]
    index = int(commands[1])
    value = int(commands[2])

    if command == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")

    elif command == "Strike":
        if 0 <= index < len(targets):
            if (index+value)+1 > len(targets) or index-value < 0:
                print(f"Strike missed!")
                continue
            else:
                targets = targets[:index-value] + targets[(index+value)+1:]
        else:
            print(f"Strike missed!")