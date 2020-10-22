# #Решение 1
# operator = input()
# num_one = int(input())
# num_two = int(input())
#
#
# def calculations(num_one, num_two):
#     if operator == "multiply":
#         return num_one * num_two
#     if operator == "divide":
#         return num_one // num_two
#     if operator == "add":
#         return num_one + num_two
#     if operator == "subtract":
#         return num_one - num_two
#
#
# print(calculations(num_one, num_two))


# #Решение 2
# operator = input()
# num_one = int(input())
# num_two = int(input())
#
#
# def calculations(num_one, num_two):
#     result = None
#     if operator == "multiply":
#         result = num_one * num_two
#     elif operator == "divide":
#         result = num_one // num_two
#     elif operator == "add":
#         result = num_one + num_two
#     elif operator == "subtract":
#         result = num_one - num_two
#     return result
#
#
# print(calculations(num_one, num_two))



#Решение 3
import operator
operator_str = input()
num_one = int(input())
num_two = int(input())


def calculations(num_one, num_two):
    operator_fn = None
    if operator_str == "multiply":
        operator_fn = operator.mul
    elif operator_str == "divide":
        operator_fn = operator.floordiv
    elif operator_str == "add":
        operator_fn = operator.add
    elif operator_str == "subtract":
        operator_fn = operator.sub
    return operator_fn(num_one, num_two)


print(calculations(num_one, num_two))