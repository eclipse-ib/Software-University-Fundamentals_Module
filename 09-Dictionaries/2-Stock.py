products = input().split()
dict_prod = {products[i]: int(products[i+1]) for i in range(0, len(products), 2)}

searched_products = input().split()
for s_product in searched_products:
    quantity = dict_prod.get(s_product)
    if quantity:
        print(f"We have {dict_prod[s_product]} of {s_product} left")
    else:
        print(f"Sorry, we don't have {s_product}")