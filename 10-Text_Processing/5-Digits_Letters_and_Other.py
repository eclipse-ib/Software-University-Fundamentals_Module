text = input()

digits = ""
chars = ""
others = ""

for i in text:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        chars += i
    else:
        others += i
print(f"""
{digits}
{chars}
{others}
""")