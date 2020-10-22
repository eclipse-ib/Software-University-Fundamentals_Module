dwarfs = {}

while True:
    data = input().split(" <:> ")
    if data[0] == "Once upon a time":
        break
    dwarf_name = data[0]
    dwarf_hat_color = data[1]
    dwarf_physics = int(data[2])
    if dwarf_name not in dwarfs:
        dwarfs[(dwarf_name, dwarf_hat_color)] = dwarf_physics
    elif dwarf_name in dwarfs:
        if dwarfs[dwarf_name][0] != dwarf_hat_color:
            dwarfs[dwarf_name] = [dwarf_hat_color, dwarf_physics]
        elif dwarfs[dwarf_name][0] == dwarf_hat_color:
            if int(dwarfs[dwarf_name][1]) < dwarf_physics:
                dwarfs[dwarf_name] = [dwarf_hat_color, dwarf_physics]


for k, v in sorted(dwarfs.items(), key=lambda item: (-item[1], item[0][1])):
    print(f"({k[1]}) {k[0]} <-> {v}")