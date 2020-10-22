num_1: int = int(input())
num_2: int = int(input())
num_3: int = int(input())


def sum_numbers(num_1, num_2):
    result = num_1 + num_2
    return result


def subtract(num_1, num_2):
    result_subtract = num_1 - num_2
    return result_subtract


def add_and_subtract(num_1, num_2, num_3):
    sum = sum_numbers(num_1, num_2)
    print(subtract(sum, num_3))


add_and_subtract(num_1, num_2, num_3)



# def sum_numbers(num_1, num_2, num_3):
#     result = (num_1 + num_2) - num_3
#     return result
#
#
# num_1: int = int(input())
# num_2: int = int(input())
# num_3: int = int(input())
# print(sum_numbers(num_1, num_2, num_3))