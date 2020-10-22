# С друг регекс:
import re

s = input()
search_patter = "(\\b[A-Z][a-z]+ [A-Z][a-z]+\\b)"
x = re.findall(search_patter, s)
print(' '.join(x))