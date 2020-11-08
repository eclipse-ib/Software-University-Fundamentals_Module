bands = {}

total_playtime = 0

while True:
    commands = input().split("; ")
    if "start of concert" in commands:
        break

    band_name = commands[1]

    if commands[0] == "Add":
        if band_name not in bands:
            bands[band_name] = {}
            bands[band_name]["members"] = commands[2].split(", ")
            bands[band_name]["members"] = list(dict.fromkeys(bands[band_name]["members"]))
        else:
            if "members" in bands[band_name]:
                bands[band_name]["members"] += commands[2].split(", ")
                bands[band_name]["members"] = list(dict.fromkeys(bands[band_name]["members"]))
            else:
                bands[band_name]["members"] = commands[2].split(", ")
                bands[band_name]["members"] = list(dict.fromkeys(bands[band_name]["members"]))

    elif commands[0] == "Play":
        playtime = int(commands[2])
        if band_name not in bands:
            bands[band_name] = {}
            bands[band_name]["playtime"] = playtime
            total_playtime += playtime
        else:
            if "playtime" not in bands[band_name]:
                bands[band_name]["playtime"] = playtime
                total_playtime += playtime
            else:
                bands[band_name]["playtime"] += playtime
                total_playtime += playtime

print(f"Total time: {total_playtime}")

sorted_bands = sorted(bands.keys(), key=lambda b: (-bands[b]["playtime"], b))

for x in sorted_bands:
    print(f"{x} -> {bands[x]['playtime']}")

final_input = input()

print(f"{final_input}")

for member in bands[final_input]["members"]:
    print(f"=> {member}")





