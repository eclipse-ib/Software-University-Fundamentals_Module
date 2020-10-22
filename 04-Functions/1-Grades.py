n = float(input())


def grades(n):
    if 2.00 <= n < 3.0:
        return "Fail"
    if 3.00 <= n < 3.5:
        return "Poor"
    if 3.50 <= n < 4.5:
        return "Good"
    if 4.50 <= n < 5.5:
        return "Very Good"
    if 5.50 <= n <= 6.00:
        return "Excellent"


print(grades(n))