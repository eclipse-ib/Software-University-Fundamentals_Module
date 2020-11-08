neighborhood = [int(i) for i in input().split("@")]

current_position = 0

while True:
    commands = input().split()

    if commands[0] == "Love!":
        print(f"Cupid's last position was {current_position}.")
        no_v_day_count = 0
        for v_day in neighborhood:
            if v_day != 0:
                no_v_day_count += 1
        if no_v_day_count != 0:
            print(f"Cupid has failed {no_v_day_count} places.")
        else:
            print(f"Mission was successful.")
        break

    elif commands[0] == "Jump":
        length = int(commands[1])
        for i in range(current_position, (current_position + length)):

            if current_position > len(neighborhood)-1:
                current_position = 0
                continue
            current_position += 1

        if current_position > len(neighborhood) - 1:
            current_position = 0

        if neighborhood[current_position] == 0:
            print(f"Place {current_position} already had Valentine's day.")

        else:
            neighborhood[current_position] -= 2
            if neighborhood[current_position] == 0:
                print(f"Place {current_position} has Valentine's day.")



