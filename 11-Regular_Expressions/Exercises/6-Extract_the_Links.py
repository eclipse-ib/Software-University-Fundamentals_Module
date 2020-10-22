import re

string = ""
while True:
    command = input()
    if command == "":
        break
    else:
        string += " "+command
search_patter = r"(www\.([A-Za-z0-9]+((-[A-Za-z0-9]+))*)\.([a-z]+((\.[a-z]+))*))"
for i in re.findall(search_patter, string):
    print(i[0])