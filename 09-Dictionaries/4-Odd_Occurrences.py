# Решение, което не използва defaultdict:
words = input().lower().split()
words_count = {}

for word in words:
    if word not in words_count:
        words_count[word] = 0
    words_count[word] += 1

# odd_words = []
# for word, count in words_count.items():
#     if count % 2 != 0:
#         odd_words.append(word)
# print(' '.join(odd_words))

# Вариант с list comprehension
print(' '.join([word for word, count in words_count.items() if count % 2 != 0]))




# Решение, което използва defaultdict:
# from collections import defaultdict
# words = input().lower().split()
# words_count = defaultdict(int)
#
# for word in words:
#     words_count[word] += 1
#
# # odd_words = []
# # for word, count in words_count.items():
# #     if count % 2 != 0:
# #         odd_words.append(word)
# # print(' '.join(odd_words))
#
# # Вариант с list comprehension
# print(' '.join([word for word, count in words_count.items() if count % 2 != 0]))



## Мое решение с използването на списък:
# sequence = input().lower().split()
#
# new_list = []
#
# for word in sequence:
#     count = 0
#     for i in sequence:
#         if i == word:
#             count +=1
#     if count % 2 != 0:
#         if word not in new_list:
#             new_list.append(word)
# print(' '.join(new_list))
