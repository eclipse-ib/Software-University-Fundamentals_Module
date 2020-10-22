# TANK_CAPACITY = 255
#
# n = int(input())
#
# water_in_tank = 0
#
# for i in range(1, n+1):
#     water = int(input())
#     water_in_tank += water
#     if water_in_tank > TANK_CAPACITY:
#         water_in_tank -= water
#         print(f"Insufficient capacity!")
#         continue
# print(f"{water_in_tank}")


# По-кратка версия:

TANK_CAPACITY = 255

n = int(input())

water_in_tank = 0

for i in range(n):
    water = int(input())
    if water_in_tank + water > TANK_CAPACITY:
        print(f"Insufficient capacity!")
        continue
    water_in_tank += water
print(f"{water_in_tank}")