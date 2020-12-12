import re

n = int(input())

search_patter = r"@#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z]@#{1,}"
for i in range(n):
    barcode = input()
    x = re.search(search_patter, barcode)
    if x:
        group_product = ""
        for d in barcode:
            if d.isdigit():
                group_product += d
        if group_product == "":
            group_product = "00"
        print(f"Product group: {group_product}")
    else:
        print(f"Invalid barcode")