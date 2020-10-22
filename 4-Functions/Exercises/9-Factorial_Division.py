def int_one(int_1):
    if int_1 == 0:
        return 1
    factorial_int_one = 1
    for i in range(int_1, 0, -1):
        factorial_int_one = factorial_int_one * i
    return factorial_int_one


def int_two(int_2):
    if int_2 == 0:
        return 1
    factorial_int_two = 1
    for j in range(int_2, 0, -1):
        factorial_int_two = factorial_int_two * j
    return factorial_int_two


def factorial_result(factorial_int_one, factorial_int_two):
    result = factorial_int_one / factorial_int_two
    return result


int_1 = int(input())
int_2 = int(input())
res = factorial_result(int_one(int_1), int_two(int_2))
print(f"{res:.2f}")
# print(f"{factorial_result(int_one(int_1), int_two(int_2)):.2f}")