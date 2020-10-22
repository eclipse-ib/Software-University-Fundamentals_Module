# Мое решение:
products = {}

while True:
    product_no_splt = input()
    if product_no_splt == "statistics":
        break
    key, value = product_no_splt.split(": ")

    if key not in products:
        products[key] = int(value)
    else:
        products[key] += int(value)

print(f"Products in stock:")
for (k, v) in products.items():
    print(f"- {k}: {v}")
print(f"Total Products: {len(products)}")
## total_quantity = 0
## for val in products.values():
##     total_quantity += int(val)
# total_quantity = sum(products.values())
print(f"Total Quantity: {sum(products.values())}")




# # Решение с използването на библиотека:
# from collections import defaultdict
#
# products = defaultdict(int)
#
# while True:
#     product = input()
#     if product == "statistics":
#         break
#     key, value = product.split(": ")
#
#     products[key] += int(value)
#
# print(f"Products in stock:")
# for (k, v) in products.items():
#     print(f"- {k}: {v}")
# print(f"Total Products: {len(products)}")
# print(f"Total Quantity: {sum(products.values())}")