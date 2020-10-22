number_of_commands = int(input())

registered = {}

for i in range(number_of_commands):
    command = input().split(maxsplit=3)
    reg_command = command[0]
    name = command[1]
    if reg_command == "register":
        plate_number = command[2]
        if name not in registered:
            registered[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered[name]}")

    elif reg_command == "unregister":
        if name not in registered:
            print(f"ERROR: user {name} not found")
        else:
            del registered[name]
            print(f"{name} unregistered successfully")

for k, v in registered.items():
    print(f"{k} => {v}")