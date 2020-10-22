number: int = int(input())


def sum_even_odd(number):
    even_sum = 0
    odd_sum = 0
    for i in str(number):
        if int(i) % 2 == 0:
            even_sum += int(i)
        elif int(i) % 2 != 0:
            odd_sum += int(i)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(f"{sum_even_odd(number)}")