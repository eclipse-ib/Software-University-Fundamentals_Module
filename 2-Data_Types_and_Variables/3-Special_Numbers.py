# Вариант 1
# n = int(input())
#
# for number in range(1, n+1):
#     sum_of_digits = 0
#     for c in str(number):
#         sum_of_digits += int(c)
#     is_special = sum_of_digits in (5, 7, 11)
#     print(f"{number} -> {is_special}")



## Вариант 2 с int(number_copy / 10) на 23 ред:
n = int(input())

for number in range(1, n+1):
    sum_of_digits = 0

    number_copy = number
    while number_copy > 0:
        digit = number_copy % 10
        sum_of_digits += digit
        number_copy = int(number_copy / 10)
    ## PB вариант без да вкараме данните в tupal:
    ## is_special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11
    ## Със tupal:
    is_special = sum_of_digits in (5, 7, 11)
    print(f"{number} -> {is_special}")

## Вариант 3 с number_copy // 10 на 40 ред:
n = int(input())

for number in range(1, n+1):
    sum_of_digits = 0

    number_copy = number
    while number_copy > 0:
        digit = number_copy % 10
        sum_of_digits += digit
        number_copy = number_copy // 10
    ## PB вариант без да вкараме данните в tupal:
    ## is_special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11
    ## Със tupal:
    is_special = sum_of_digits in (5, 7, 11)
    print(f"{number} -> {is_special}")
