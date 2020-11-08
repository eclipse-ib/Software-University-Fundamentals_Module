stops = input()

while True:
    commands = input().split(":")
    if commands[0] == "Travel":
        print(f"Ready for world tour! Planned stops: {stops}")
        break

    command = commands[0]

    if "Add" in command:
        index = int(commands[1])
        add_string = commands[2]
        if 0 <= index <= len(stops)-1:
            stops = stops[:index] + add_string + stops[index:]
        print(stops)

    elif "Remove" in command:
        start_index = int(commands[1])
        end_index = int(commands[2])
        if 0 <= start_index <= len(stops)-1 and 0 <= end_index <= len(stops)-1:
            stops = stops.replace(stops[start_index:end_index+1], "")
        print(stops)

    elif "Switch" in command:
        old_string = commands[1]
        new_string = commands[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)



