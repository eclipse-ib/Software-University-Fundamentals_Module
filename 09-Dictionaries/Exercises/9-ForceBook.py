sides = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        command = command.split(" | ", maxsplit=2)
        force_side = command[0]
        force_user = command[1]
        if force_side not in sides:
            sides[force_side] = [force_user]
            # if force_user not in sides.values():
            #     sides[force_side] = [force_user]
            # else:
            #     sides[force_side] = []
        else:
            if force_user not in sides[force_side]:
                sides[force_side].append(force_user)

    elif "->" in command:
        command = command.split(" -> ", maxsplit=2)
        force_side = command[1]
        force_user = command[0]

        old_side = ""

        for key, value in sides.items():
            if force_user in value:
                old_side = key
                break
        if old_side != "":
            sides[old_side].remove(force_user)
            if force_side not in sides:
                sides[force_side] = []
            sides[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        else:
            if force_side not in sides:
                sides[force_side] = []
            sides[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")


for key, value in sorted(sides.items(), key=lambda item: (-len(item[1]), item[0])):
    if len(value) == 0:
        continue
    print(f"Side: {key}, Members: {len(value)}")
    for user in sorted(value):
        print(f"! {user}")