def name_length():
    if 2 < len(name) < 17:
        return True
    else:
        return False


def contains_characters():
    for character in name:
        if character.isalnum() or character == "_" or character == "-":
            pass
        else:
            return False
        if character == " ":
            return False
    return True


names = input().split(", ")

for name in names:
    if name_length():
        pass
    else:
        continue

    if contains_characters():
        pass
    else:
        continue
    print(name)