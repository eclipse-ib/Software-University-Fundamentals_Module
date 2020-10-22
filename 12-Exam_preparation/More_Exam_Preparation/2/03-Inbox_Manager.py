users_and_emails = {}

while True:
    commands = input().split("->")
    command = commands[0]
    if command == "Statistics":
        break

    username = commands[1]

    if command == "Add":
        if username in users_and_emails:
            print(f"{username} is already registered")
        else:
            users_and_emails[username] = []

    elif command == "Send":
        email = commands[2]
        users_and_emails[username].append(email)

    elif command == "Delete":
        if username not in users_and_emails:
            print(f"{username} not found!")
        else:
            del users_and_emails[username]

print(f"Users count: {len(users_and_emails)}")

for k, v in sorted(users_and_emails.items(), key=lambda item: (-len(item[1]), item)):
    print(k)
    for email in v:
        print(f"- {email}")