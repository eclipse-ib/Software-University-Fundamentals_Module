email = input()

while True:
    commands = input().split()
    command = commands[0]
    if command == "Complete":
        break

    if command == "Make":
        case = commands[1]
        if case == "Upper":
            email = email.upper()
        elif case == "Lower":
            email = email.lower()
        print(email)

    elif command == "GetDomain":
        count = int(commands[1])
        print(email[-count:])

    elif command == "GetUsername":
        if "@" not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            splitted_email = email.split("@")
            print(f"{splitted_email[0]}")

    elif command == "Replace":
        char = commands[1]
        email = email.replace(char, "-")
        print(email)

    elif command == "Encrypt":
        for s in email:
            print(ord(s), end=" ")
