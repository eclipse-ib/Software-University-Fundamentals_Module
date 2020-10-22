items = input().split("|")
budget = float(input())

virtual_budget = budget
profit = 0

for i in items:
    item = i.split("->")
    if float(item[1]) <= 50.00 and item[0] == "Clothes":
        if virtual_budget < float(item[1]):
            continue
        else:
            virtual_budget -= float(item[1])
            profit += ((float(item[1]) * 1.4) - float(item[1]))
    elif float(item[1]) <= 35.00 and item[0] == "Shoes":
        if virtual_budget < float(item[1]):
            continue
        else:
            virtual_budget -= float(item[1])
            profit += ((float(item[1]) * 1.4) - float(item[1]))
    elif float(item[1]) <= 20.50 and item[0] == "Accessories":
        if virtual_budget < float(item[1]):
            continue
        else:
            virtual_budget -= float(item[1])
            profit += ((float(item[1]) * 1.4) - float(item[1]))
    else:
        continue
    item_final_price = float(item[1]) * 1.4
    print(f"{item_final_price:.2f} ", end="")
print()
print(f"Profit: {profit:.2f}")
if budget + profit >= 150:
    print(f"Hello, France!")
else:
    print(f"Time to go.")