notes = {}


while True:
    command_nosplt = input()
    if command_nosplt == "END":
        break
    command = command_nosplt.split("->", maxsplit=2)
    if "Add" in command:
        if command[1] in notes.keys():
            notes[command[1]] += ","+command[2]
        else:
            notes[command[1]] = command[2]
    elif "Remove" in command:
        if command[1] in notes.keys():
            del notes[command[1]]

sorted_by_values = sorted(notes.items(), key=lambda item: (len(item[1]), item[0]), reverse=True)
print(f"Stores list:")
for i in sorted_by_values:
    print(i[0])
    for j in i[1].split(","):
        print(f"<<{j}>>")