raw_activation_key = input()

while True:
    commands = input().split(">>>")
    if commands[0] == "Generate":
        print(f"Your activation key is: {raw_activation_key}")
        break

    command = commands[0]

    if command == "Contains":
        substring = commands[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command == "Flip":
        start_index = int(commands[2])
        end_index = int(commands[3])
        if commands[1] == "Upper":
            raw_activation_key = raw_activation_key[:start_index] +\
            raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]
            print(raw_activation_key)
        elif commands[1] == "Lower":
            raw_activation_key = raw_activation_key[:start_index] + \
            raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]
            print(raw_activation_key)

    elif command == "Slice":
        slice_start_index = int(commands[1])
        slice_end_index = int(commands[2])
        raw_activation_key = raw_activation_key.replace(raw_activation_key\
        [slice_start_index:slice_end_index], "")
        print(raw_activation_key)

