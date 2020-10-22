text = input()

encrypted_text = ""

for i in text:
    encrypted_char = ord(i) + 3
    encrypted_text += chr(encrypted_char)
print(encrypted_text)