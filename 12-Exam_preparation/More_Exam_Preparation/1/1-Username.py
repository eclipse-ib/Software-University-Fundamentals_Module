original_username = input()

while True:
    commands = input().split()
    if commands[0] == "Sign":
        break

    command = commands[0]

    if command == "Case":
        case_command = commands[1]

        if case_command == "lower":
            original_username = original_username.lower()
        else:
            original_username = original_username.upper()
        print(original_username)

    elif command == "Reverse":
        start_index = int(commands[1])
        end_index = int(commands[2])
        if start_index <= 0 and end_index > len(original_username)-1:
            continue
        else:
            reversed_o_u = original_username[start_index:end_index+1]
            print(reversed_o_u[::-1])

    elif command == "Cut":
        substring = commands[1]
        if substring in original_username:
            original_username = original_username.replace(substring, "")
            print(original_username)
        else:
            print(f"The word {original_username} doesn't contain {substring}.")

    elif command == "Replace":
        char = commands[1]
        original_username = original_username.replace(char, "*")
        print(original_username)

    elif command == "Check":
        check_char = commands[1]
        if check_char in original_username:
            print(f"Valid")
        else:
            print(f"Your username must contain {check_char}.")