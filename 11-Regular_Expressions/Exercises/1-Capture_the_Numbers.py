import re

string = ""
while True:
    command = input()
    if command == "":
        break
    else:
        string += " "+command
search_patter = r"\d+"
for i in re.findall(search_patter, string):
    print(i, end=" ")