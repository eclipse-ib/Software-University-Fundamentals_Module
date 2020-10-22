# PB method с изваждане на променлива:
# word = input()
#
# repeated_word = ""
#
# for i in word:
#     current_char = i * 2
#     repeated_word = repeated_word + current_char
# print(repeated_word)

# new method с директно принтиране:
word = input()

for i in word:
    print(i * 2, end="")