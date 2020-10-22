import re

inputs = int(input())

regex = r"((.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^><]{3})<\2)"

for i in range(inputs):
    text = input()
    is_it_regex = re.findall(regex, text)
    if is_it_regex:
        for reg in is_it_regex:
            encrypt_reg = reg[2]+reg[3]+reg[4]+reg[5]
            print(f"Password: {encrypt_reg}")
    else:
        print(f"Try another password!")