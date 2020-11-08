targets = [int(i) for i in input().split("|")]

points = 0

while True:
    commands = input().split()
    if "Game" in commands[0]:
        targets = [str(i) for i in targets]
        print(" - ".join(targets))
        print(f"Iskren finished the archery tournament with {points} points!")
        break
    if "Shoot" in commands[0]:
        l_or_r, start_index, length = commands[1].split("@")

        if "Left" == l_or_r:
            if int(start_index) > len(targets) or int(start_index) < 0:
                continue
            else:
                target = int(start_index)
                current_target = 0
                for i in range(int(length)):
                    target -= 1
                    if target == -1:
                        target = len(targets)-1
                    current_target = targets[target]
                if targets[target] < 5:
                    points += targets[target]
                    targets[target] = 0
                    continue
                targets[target] -= 5
                points += 5

        elif "Right" == l_or_r:
            if int(start_index) > len(targets) or int(start_index) < 0:
                continue
            else:
                target_right = int(start_index)
                current_target_right = 0
                for i in range(int(length)):
                    target_right += 1
                    if target_right > len(targets)-1:
                        target_right = 0
                    current_target_right = targets[target_right]
            if targets[target_right] < 5:
                points += targets[target_right]
                targets[target_right] = 0
                continue
            targets[target_right] -= 5
            points += 5

    elif "Reverse" == commands[0]:
        targets = targets[::-1]

