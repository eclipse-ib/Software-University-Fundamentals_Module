products = {}

while True:
    command = input().split(maxsplit= 3)
    if command[0] == "buy":
        break
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product not in products:
        products[product] = [price, quantity]
    else:
        (products[product])[0] = price
        (products[product])[1] += int(quantity)

for k, v in products.items():
    new_v = v[0] * v[1]
    print(f"{k} -> {new_v:.2f}")