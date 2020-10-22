text = input()
new_text = ""

last_char = ""

for i in text:
    if i != last_char:
        new_text += i
        last_char = i
print(new_text)