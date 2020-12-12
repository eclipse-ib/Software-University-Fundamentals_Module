string = input()

while True:
    commands = input().split()
    command = commands[0]
    if command == "Done":
        print(f"Your password is: {string}")
        break

    if command == "TakeOdd":
        new_password = ""
        for index, odd in enumerate(string):
            if index % 2 != 0:
                new_password += odd
        string = new_password
        print(string)

    elif command == "Cut":
        cut_index = int(commands[1])
        cut_length = int(commands[2])
        string = string[0:cut_index] + string[cut_index + cut_length:]
        print(string)

    elif command == "Substitute":
        substring = commands[1]
        substitute = commands[2]

        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print(f"Nothing to replace!")
