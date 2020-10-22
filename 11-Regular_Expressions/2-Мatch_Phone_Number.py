import re

s = input()
search_patter = r"(\+359-2-[0-9]{3}-[0-9]{4}\b|\+359 2 [0-9]{3} [0-9]{4}\b)"
x = re.findall(search_patter, s)
print(', '.join(x))