numbers = [int(i) for i in input().split()]

average = sum(numbers) / len(numbers)
all_greater_than_average = [greater for greater in numbers if greater > average]
top_five = []
for j in range(5):
    if len(all_greater_than_average) == 0:
        break
    top_five.append(str(max(all_greater_than_average)))
    all_greater_than_average.remove(max(all_greater_than_average))

if len(top_five) == 0:
    print("No")
else:
    print(" ".join(top_five))

