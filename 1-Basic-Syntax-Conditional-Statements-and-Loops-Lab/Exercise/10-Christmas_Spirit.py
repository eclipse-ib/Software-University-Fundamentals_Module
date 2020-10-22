type_quantity = int(input())
days = int(input())

spirit = 0
money = 0

for i in range(1, days+1):
    if i % 11 == 0:
        type_quantity += 2
    if i % 2 == 0:
        spirit += 5
        money = money + (2*type_quantity)
    if i % 3 == 0:
        spirit += 13
        money = money + ((5*type_quantity) + (3*type_quantity))
    if i % 5 == 0:
        spirit += 17
        money = money + (15*type_quantity)
        if i % 5 == 0 and i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        money = money + 23
if days % 10 == 0:
    spirit -= 30
print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")