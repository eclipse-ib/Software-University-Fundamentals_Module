import re

n = int(input())

regex = r"!(?P<command>[A-Z][a-z]{2,})!:\[(?P<command_message>[A-Za-z]{8,})\]"

for _ in range(n):
    message = input()
    r = re.findall(regex, message)

    if r:
        print(f"{r[0][0]}: {' '.join([str(ord(i)) for i in r[0][1]])}")

    else:
        print(f"The message is invalid")
