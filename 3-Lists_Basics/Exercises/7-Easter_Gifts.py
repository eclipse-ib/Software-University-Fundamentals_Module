gifts = input().split()


while True:
    command = input()
    list_command = command.split()
    if command == "No Money":
        break
    elif "OutOfStock" in command:
        none_gift = list_command[1]
        if none_gift in gifts:
            for i, j in enumerate(gifts, 0):
                if j == none_gift:
                    gifts[i] = "None"
    elif "Required" in command:
        gift_index = list_command[2]
        if 0 < int(gift_index) < len(gifts):
            new_gift = list_command[1]
            gifts.pop(int(gift_index))
            gifts.insert(int(gift_index), new_gift)
        else:
            pass
    elif "JustInCase" in command:
        replace_gift = list_command[1]
        gifts.pop()
        gifts.append(replace_gift)
while "None" in gifts:
    gifts.remove("None")
new_list_gifts = " ".join(gifts)
print(f"{new_list_gifts}")