# Нов и лесен метод с използването на []:
# word = input()
#
# reversed_word = ""
#
# for i in range(len(word) - 1, -1, -1):
#     reversed_word += word[i]
# print(reversed_word)



# Още по-лесен метод с използване на билдин функцията "reversed":
word = input()
reversed_word = ""

for i in reversed(word):
    reversed_word += i
print(reversed_word)


# Супер лесен метод:
# word = input()[::-1]
# print(f"{word}")