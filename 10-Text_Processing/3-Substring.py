# Решение с функция:
def replace_function(string_one, string_two):
    while string_one in string_two:
        string_two = string_two.replace(string_one, "")
    return string_two


print(replace_function(input(), input()))


# # Решение 1
# string_one = input()
# string_two = input()
#
# while string_one in string_two:
#     string_two = string_two.replace(string_one, "")
# print(string_two)