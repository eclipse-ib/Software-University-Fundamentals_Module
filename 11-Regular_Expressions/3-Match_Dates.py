import re

text = input()
search_patter = r"((\d{2})([-/\.])([A-Z][a-z]{2})\2(\d{4}))"
x = re.findall(search_patter, text)
str_x = ', '.join(x)
split_x = re.split(", ", str_x)
for i in split_x:
    print(i)
