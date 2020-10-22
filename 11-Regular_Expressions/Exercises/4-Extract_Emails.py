import re

string = input()

regex = r"\s(([A-Za-z0-9]+((\.|-|_)\w+)*)@((\w+)((\.|-)\w+)*)\.(\w+((\.|-)\w+)*))\b"

for i in re.findall(regex, string, re.IGNORECASE):
    print(i[0])