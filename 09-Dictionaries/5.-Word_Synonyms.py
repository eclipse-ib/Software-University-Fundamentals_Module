# Трето решение с използването на defaultdict:
from collections import defaultdict
synonyms = defaultdict(list)

number_of_words = int(input())

for i in range(number_of_words):
    word = input()
    synonym = input()
    synonyms[word].append(synonym)

for (key, values) in synonyms.items():
    print(f"{key} - {', '.join(values)}")





# Второ решение:
# synonyms = {}
#
# number_of_words = int(input())
#
# for i in range(number_of_words):
#     word = input()
#     synonym = input()
#     if word not in synonyms.keys():
#         synonyms[word] = synonym
#     else:
#         synonyms[word] += ", " + synonym
#
# for (key, values) in synonyms.items():
#     print(f"{key} - {values}")




# # Първо мое решение:
# synonyms = {}
#
# number_of_words = int(input())
# old_index_key = ""
#
# for i in range(1, 2 * number_of_words+1):
#     word = input()
#
#     if i % 2 != 0:
#         if word not in synonyms.keys():
#             synonyms[word] = ""
#             old_index_key = word
#         old_index_key = word
#     else:
#         if old_index_key in synonyms.keys():
#             if synonyms[old_index_key] == "":
#                 synonyms[old_index_key] += word
#             else:
#                 synonyms[old_index_key] += ", " + word
#
# for (key, values) in synonyms.items():
#     print(f"{key} - {values}")
