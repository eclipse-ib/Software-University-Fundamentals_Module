def order_price(product, quantity):
    price = None
    if product == "coffee":
        price = quantity * 1.50
    elif product == "water":
        price = quantity * 1.00
    elif product == "coke":
        price = quantity * 1.40
    elif product == "snacks":
        price = quantity * 2.00
    return price


product: str = input()
quantity: int = int(input())
print(f"{order_price(product, quantity):.2f}")