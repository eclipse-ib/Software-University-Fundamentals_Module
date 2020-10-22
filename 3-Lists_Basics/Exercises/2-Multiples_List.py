factor = int(input())
count = int(input())
list = []
counter = factor

for _ in range(count):
    list.append(counter)
    counter += factor
print(list)