import re

string = input()
search_patter = r"\b_([A-Za-z0-9]+)\b"
print(','.join(re.findall(search_patter, string)))