import re

mirror_words = ""

text = input()

regex = r"([@|#])(?P<word_one>[A-Za-z]{3,})(\1)([@|#])(?P<word_two>[A-Za-z]{3,})(\1)"

matches = re.finditer(regex, text)
all_matches = 0
for match in matches:
    all_matches += 1
    if match.group("word_one") == match.group("word_two")[::-1]:
        mirror_words += f"{match.group('word_one')} <=> {match.group('word_two')}, "

if re.search(regex, text) is not None:
    print(f"{all_matches} word pairs found!")
    if mirror_words == "":
        print(f"No mirror words!")
    else:
        print(f"The mirror words are:")
        print(f"{mirror_words[:-2]}")
else:
    print(f"No word pairs found!\nNo mirror words!")