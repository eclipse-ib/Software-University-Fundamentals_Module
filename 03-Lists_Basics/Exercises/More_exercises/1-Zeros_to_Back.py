numbers = input().split(", ")
new_numbers = []

for i in numbers:
    if int(i) == 0:
        pass
    else:
        new_numbers.append(int(i))
for i in numbers:
    if int(i) == 0:
        new_numbers.append(0)
print(f"{new_numbers}")
