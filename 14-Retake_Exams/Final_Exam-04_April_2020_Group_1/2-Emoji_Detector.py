import re

text = input()

regex = r"(?P<match>(\:\:|\*\*)(?P<name>[A-Z][a-z]{2,})(\2))"

threshold = 1
for i in text:
    if i.isdigit():
        threshold = threshold * int(i)
print(f"Cool threshold: {threshold}")

matches = 0
cool_emojis = []
for match in re.finditer(regex, text, re.MULTILINE):
    matches +=1
    ascii_values_sum = 0
    for symb in match.group("name"):
        ascii_values_sum += ord(symb)
    if ascii_values_sum >= threshold:
        cool_emojis.append(match.group("match"))

if cool_emojis != None:
    print(f"{matches} emojis found in the text. The cool ones are:")
    for i in cool_emojis:
        print(i)