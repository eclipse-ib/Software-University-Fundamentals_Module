import re

s = input()
search_patter = r"(((^|(?<=\s))(-*)(\d+))((\.\d+)*)($|(?=\s)))"
for i in re.findall(search_patter, s):
    number = i[0]
    print(f"{number}", end=" ")