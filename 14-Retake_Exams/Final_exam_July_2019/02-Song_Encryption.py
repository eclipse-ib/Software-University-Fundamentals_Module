import re

regex = r"(?P<valid_song>(?P<artist>^[A-Z][a-z]+(\s[a-z']+)*(?=\b)):(?P<song>\b[A-Z]+(\s[A-Z]+)*)\b)"

while True:
    commands = input()
    if commands == "end":
        break
    if re.search(regex, commands) is None:
        print(f"Invalid input!")
        continue
    else:
        valid_song = re.finditer(regex, commands, re.MULTILINE)
        if valid_song:

            for match in valid_song:
                key = len(match.group("artist"))
                encrypted_song = ""
                for symbol in match.group("valid_song"):
                    if symbol == " ":
                        encrypted_song += " "
                        continue

                    if symbol == "'":
                        encrypted_song += "'"
                        continue

                    if symbol == ":":
                        encrypted_song += "@"
                        continue

                    if symbol.isupper() and ord(symbol) + key > 90:
                        new_chr = ((ord(symbol)+key) - 90) + 64
                        encrypted_song += chr(new_chr)
                        continue
                    if symbol.islower() and ord(symbol) + key > 122:
                        new_chr = ((ord(symbol) + key) - 122) + 96
                        encrypted_song += chr(new_chr)
                        continue
                    new_chr = ord(symbol)+key
                    encrypted_song += chr(new_chr)
                print(f"Successful encryption: {encrypted_song}")