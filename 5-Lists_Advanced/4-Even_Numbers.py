numbers = input().split(", ")

even_indices = [int(index) for index, n in enumerate(numbers) if int(n) % 2 == 0]
print(even_indices)