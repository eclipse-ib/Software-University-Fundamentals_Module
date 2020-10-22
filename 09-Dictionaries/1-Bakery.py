# Решение с използването на dict comprehension:

products = input().split()
dict_products = {products[i]: int(products[i+1]) for i in range(0, len(products), 2)}

print(dict_products)

# Нормално решение с използването на for цикъл
# products = input().split()
#
# dict_products = {}
# key_index = 0
#
# # for i in range(len(products)//2):
# for i in range(0, len(products), 2):
#     dict_products[products[key_index]] = int(products[key_index+1])
#     key_index += 2
#
# print(dict_products)