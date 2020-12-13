email = input()

while True:
    tokens = input().split()
    if tokens[0] == "Complete":
        break

    command = tokens[0]

    if command == "Make":
        case = tokens[1]

        if case == "Upper":
            email = email.upper()
            print(email)

        elif case == "Lower":
            email = email.lower()
            print(email)

    elif command == "GetDomain":
        count = int(tokens[1])
        print(email[-count:])

    elif command == "GetUsername":
        if "@" in email:
            username = ""
            for i in email:
                if i == "@":
                    break
                username += i
            print(username)

        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif command == "Replace":
        char = tokens[1]
        email = email.replace(char, "-")
        print(email)

    elif command == "Encrypt":
        encrypted_email = [str(ord(j)) for j in email]
        print(' '.join(encrypted_email))
