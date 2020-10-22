number: int = int(input())


def divisor_numbers(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors


def sum_divisors(number):
    sum_div = sum(divisor_numbers(number))
    if sum_div == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(sum_divisors(number))
