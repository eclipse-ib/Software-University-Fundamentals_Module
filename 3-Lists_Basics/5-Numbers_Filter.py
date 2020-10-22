## Още по-хитър метод с по-малко код:
n = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"
numbers = []
for _ in range(n):
    number = int(input())
    numbers.append(number)
command = input()
filtered = []
for number in numbers:
    filter_passes = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_NEGATIVE and number < 0) or
        (command == COMMAND_POSITIVE and number >= 0)
    )
    if filter_passes:
        filtered.append(number)
print(filtered)


## По-хитър метод:

n = int(input())

numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)
command = input()
filtered = []
for number in numbers:
    if command == "even" and number % 2 == 0:
        filtered.append(number)
    elif command == "odd" and number % 2 != 0:
        filtered.append(number)
    elif command == "negative" and number < 0:
        filtered.append(number)
    elif command == "positive" and number >= 0:
        filtered.append(number)
print(filtered)

# Дълъг метод:
# n = int(input())
#
# even= []
# odd = []
# negative = []
# positive = []
#
#
# for _ in range(n):
#     number = int(input())
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
#     if number >= 0:
#         positive.append(number)
#     else:
#         negative.append(number)
# command = input()
# if command == "even":
#     print(even)
# elif command == "odd":
#     print(odd)
# elif command == "positive":
#     print(positive)
# else:
#     print(negative)