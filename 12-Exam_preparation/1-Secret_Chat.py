message = input()

while True:
    command = input().split(":|:")

    if command[0] == "Reveal":
        break

    general_command = command[0]

    if general_command == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]

    elif general_command == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message = message[:] + substring[::-1]
        else:
            print(f"error")
            continue

    elif general_command == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in message:
            message = message.replace(substring, replacement)
    print(message)

print(f"You have a new text message: {message}")