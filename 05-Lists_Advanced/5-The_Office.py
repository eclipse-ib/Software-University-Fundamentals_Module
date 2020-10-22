happiness = input().split()
factor = int(input())

happiness_int = list(map(lambda x: int(x) * factor, happiness))
average = sum(happiness_int) / len(happiness_int)
happy_employees = list(filter((lambda x: x >= average), happiness_int))
if len(happy_employees) >= len(happiness_int) / 2:
    print(f"Score: {len(happy_employees)}/{len(happiness_int)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(happiness_int)}. Employees are not happy!")