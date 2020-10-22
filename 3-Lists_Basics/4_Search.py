##Най-оптимизирания начин:
n = int(input())
word = input()

new_list = []
filtered_strings = []

for _ in range(n):
    new_sentence = input()
    new_list.append(new_sentence)
    if word in new_sentence:
        filtered_strings.append(new_sentence)
print(new_list)
print(filtered_strings)


## Решение по условие:
# n = int(input())
# word = input()
#
# new_list = []
# filtered_strings = []
#
# for _ in range(n):
#     new_sentence = input()
#     new_list.append(new_sentence)
#     if word in new_sentence:
#         filtered_strings.append(new_sentence)
# print(new_list)
# for i in range(len(new_list)-1, -1, -1):
#     element = new_list[i]
#     if word not in element:
#         new_list.remove(element)
# print(new_list)

## Друго решение:

# n = int(input())
# word = input()
#
# new_list = []
# filtered_strings = []
#
# for _ in range(n):
#     new_sentence = input()
#     new_list.append(new_sentence)
#     if word in new_sentence:
#         filtered_strings.append(new_sentence)
# print(new_list)
# for i in new_list:
#     if word in i:
#         filtered_strings.append(i)
# print(filtered_strings)
