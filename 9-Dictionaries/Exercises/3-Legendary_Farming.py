def leg_items():
    if l_dict["shards"] >= 250 or l_dict["fragments"] >= 250\
            or l_dict["motes"] >= 250:
        return True
    else:
        return False


def found_l_i():
    if l_dict["shards"] >= 250:
        return "Shadowmourne"
    elif l_dict["fragments"] >= 250:
        return "Valanyr"
    elif l_dict["motes"] >= 250:
        return "Dragonwrath"


def key_with_max_val(l_dict):
    v = list(l_dict.values())
    k = list(l_dict.keys())
    max_key = k[v.index(max(v))]
    l_dict[max_key] -= 250


def del_l_items():
    if "shards" in doc_materials.keys():
        del doc_materials["shards"]
    if "fragments" in doc_materials.keys():
        del doc_materials["fragments"]
    if "motes" in doc_materials.keys():
        del doc_materials["motes"]


l_dict = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

doc_materials = {}

materials = input().lower().split()


while True:
    quantity_index = 0
    material_index = 1

    for line in range(len(materials)//2):
        quantity = int(materials[quantity_index])
        material = materials[material_index]

        if material not in doc_materials:
            doc_materials[material] = quantity
        else:
            doc_materials[material] += quantity

        if material == "shards":
            l_dict["shards"] += quantity
        elif material == "fragments":
            l_dict["fragments"] += quantity
        elif material == "motes":
            l_dict["motes"] += quantity

        if leg_items() == True:
            print(f"{found_l_i()} obtained!")
            key_with_max_val(l_dict)
            for k, v in sorted(l_dict.items(), key=lambda item: (-item[1], item[0])):
                print(f"{k}: {v}")

            del_l_items()

            for k, v in sorted(doc_materials.items()):
                print(f"{k}: {v}")
            exit()
        else:
            quantity_index += 2
            material_index += 2
    materials = input().lower().split()