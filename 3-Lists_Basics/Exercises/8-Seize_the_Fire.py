type_of_fire = input().split("#")
water_amount = int(input())

effort = 0
total_fire = 0

print(f"Cells:")
for i in type_of_fire:
    cell = i.split(" ")
    if water_amount <= 0:
        break
    if 0 < int(cell[2]) <= 50 and cell[0] == "Low":
        if int(cell[2]) > water_amount:
            continue
        else:
            water_amount -= int(cell[2])
            effort += (int(cell[2]) / 4)
            total_fire += int(cell[2])
            print(f" - {cell[2]}")
    elif 50 < int(cell[2]) <= 80 and cell[0] == "Medium":
        if int(cell[2]) > water_amount:
            continue
        else:
            water_amount -= int(cell[2])
            effort += (int(cell[2]) / 4)
            total_fire += int(cell[2])
            print(f" - {cell[2]}")
    elif 80 < int(cell[2]) <= 125 and cell[0] == "High":
        if int(cell[2]) > water_amount:
            continue
        else:
            water_amount -= int(cell[2])
            effort += (int(cell[2]) / 4)
            total_fire += int(cell[2])
            print(f" - {cell[2]}")
print(f"Effort: {effort:.2f}\nTotal Fire: {total_fire}")