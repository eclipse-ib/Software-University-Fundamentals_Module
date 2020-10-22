strings = input()

final_sum = 0

string_one, string_two = strings.split()
index = 0
if len(string_one) == len(string_two):
    for i in range(len(string_two)):
        current_sum = ord(string_one[index]) * ord(string_two[index])
        final_sum += current_sum
        index += 1
else:
    rng = 0
    if len(string_one) > len(string_two):
        rng = len(string_two)
        for j in range(rng):
            current_sum = ord(string_one[index]) * ord(string_two[index])
            final_sum += current_sum
            index += 1
        last_range = len(string_one) - len(string_two)
        for last in range(last_range):
            current_sum = ord(string_one[index])
            final_sum += current_sum
            index += 1
    else:
        rng = len(string_one)
        for j in range(rng):
            current_sum = ord(string_two[index]) * ord(string_one[index])
            final_sum += current_sum
            index += 1
        last_range = len(string_two) - len(string_one)
        for last in range(last_range):
            current_sum = ord(string_two[index])
            final_sum += current_sum
            index += 1

print(final_sum)