numbers = input().split()
new_list = sorted(numbers, reverse=True)
new_list = "".join(new_list)
print(new_list)