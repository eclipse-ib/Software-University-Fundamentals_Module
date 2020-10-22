strings = input().split()

total_sum = 0

for string in strings:
    first_letter_sum = 0
    last_letter_sum = 0

    number = int(string[1:-1])

    first_letter = string[0]
    last_letter = string[-1]

    if first_letter.isupper():
        first_letter_sum += number / (ord(string[0]) - 64)
    else:
        first_letter_sum += number * (ord(string[0]) - 96)

    if last_letter.isupper():
        last_letter_sum += first_letter_sum - (ord(string[-1]) - 64)
        total_sum += last_letter_sum
    else:
        last_letter_sum += first_letter_sum + (ord(string[-1]) - 96)
        total_sum += last_letter_sum


print(f"{total_sum:.2f}")