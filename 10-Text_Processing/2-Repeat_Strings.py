# Вариант с решение само на един ред:

print(''.join(map(lambda word: word * len(word), input().split())))

# Вариант с използването само на lambda + map():
# word = input().split()
# print(''.join(map(lambda word: word * len(word), word)))



# Вариант с използването на функция + map():
# def repeat_word(word):
#     return word * len(word)
#
#
# word: list = input().split()
# print(''.join(map(repeat_word, word)))


# # Мой вариант:
# strings = input().split()
#
# new_string = ""
# for string in strings:
#     new_string += string*len(string)
# print(new_string)