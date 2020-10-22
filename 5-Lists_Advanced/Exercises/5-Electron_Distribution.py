electrons = int(input())

index = 1
list_shields = []
while electrons > 0:
    shield = 2*(index**2)
    if electrons < shield:
        list_shields.append(electrons)
        electrons = 0
        break
    electrons -= shield
    list_shields.append(shield)
    index += 1
print(list_shields)