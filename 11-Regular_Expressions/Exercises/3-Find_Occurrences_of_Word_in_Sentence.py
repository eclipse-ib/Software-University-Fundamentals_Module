import re

string = input()
key_word = input()
search_patter = rf"\b{key_word}\b"
# mathes = re.findall(search_patter, string, re.IGNORECASE)
print(len(re.findall(search_patter, string, re.IGNORECASE)))