reversed_words = {}

while True:
    command = input()
    if command == "end":
        break
    reversed_words[command] = ''.join(reversed(command))

for key, value in reversed_words.items():
    print(f"{key} = {value}")