words = input()

new_list = {}

for word in words:
    if word == " ":
        continue
    if word not in new_list:
        new_list[word] = 1
    else:
        new_list[word] += 1

for (key, values) in new_list.items():
    print(f"{key} -> {values}")





## Нов и по-кратък вариант на предишното решение:
# words = input()
#
# new_list = {}
#
# for word in words:
#     if word == " ":
#         continue
#     if word not in new_list:
#         new_list[word] = 1
#     else:
#         new_list[word] += 1
#
# for (key, values) in new_list.items():
#     print(f"{key} -> {values}")




## Първи мой вариант:

# words = input()
#
# new_list = {}
#
# for word in words:
#     count = 0
#     index_chr = 0
#     index = word[index_chr]
#     if index == " ":
#         continue
#     if word == index:
#         count +=1
#         index_chr += 1
#     if word not in new_list:
#         new_list[word] = count
#     else:
#         new_list[word] += count
#
# for (key, values) in new_list.items():
#     print(f"{key} -> {values}")