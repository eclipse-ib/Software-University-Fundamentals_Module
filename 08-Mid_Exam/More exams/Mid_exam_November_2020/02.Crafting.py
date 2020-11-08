strings = input().split("|")

while True:
    commands = input().split()
    command = commands[0]

    if command == "Done":
        print(f"You crafted {''.join(strings)}!")
        break

    elif command == "Move":
        direction = commands[1]
        move_index = int(commands[2])
        if direction == "Left":
            if move_index > 0 and move_index <= len(strings)-1:
                index_value_left = strings[move_index]
                strings.remove(index_value_left)
                strings.insert(move_index-1, index_value_left)

        elif direction == "Right":
            if move_index >= 0 and move_index < len(strings) - 1:
                index_value_right = strings[move_index]
                strings.remove(index_value_right)
                strings.insert(move_index + 1, index_value_right)

    elif command == "Check":
        position = commands[1]
        if position == "Even":
            even_words = ""
            even_count = 1
            for even in range(0, len(strings)):
                if even_count % 2 != 0:
                    even_words += strings[even] + " "
                even_count += 1
            print(even_words)

        elif position == "Odd":
            odd_words = ""
            odd_count = 1
            for odd in range(0, len(strings)):
                if odd_count % 2 == 0:
                    odd_words += strings[odd] + " "
                odd_count += 1
            print(odd_words)

