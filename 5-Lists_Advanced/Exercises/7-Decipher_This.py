message = input().split()


def asci_change(message):
    numbers = [num for num in i if num.isdigit()]
    numbers_in_chr = chr(int(''.join(numbers)))
    letters = [letter for letter in i if not letter.isdigit()]
    letters_split = ''.join(letters)
    final_word = numbers_in_chr + str(letters_split)
    return final_word


def index_change(message):
    letters = [letter for letter in j]
    letters[1], letters[-1] = letters[-1], letters[1]
    letters_split = ''.join(letters)
    return letters_split



index_i = 0
for i in message:
    message[index_i] = asci_change(message)
    index_i += 1

index_j = 0
for j in message:
    message[index_j] = index_change(message)
    index_j += 1
print(' '.join(message))