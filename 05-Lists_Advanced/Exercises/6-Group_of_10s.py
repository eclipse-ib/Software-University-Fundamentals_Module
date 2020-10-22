numbers = [int(n) for n in input().split(", ")]

max_number = str(max(numbers))
first_index = 0
next_index = 10
last_index = 20
lists = []
for i in range(int(max_number[0])+1):
    lists.append([])
if int(max_number[1]) == 0:
    lists.pop(0)
for j in range(1, len(lists)+1):
    if j == 1:
        lists[first_index] = list(filter((lambda x: 0 < x <= 10), numbers))
        first_index += 1
    else:
        lists[first_index] = list(filter((lambda x: next_index < x <= last_index), numbers))
        first_index += 1
        next_index += 10
        last_index += 10

for ind, list in enumerate(lists, 1):
    print(f"Group of {ind}0's: {list}")