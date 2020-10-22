first_string = input().split(', ')
# print(first_string)
second_string = input()
# print(second_string)
final_list = []

for i in first_string:
    if i in second_string:
        final_list.append(i)

print(final_list)


list_one = input().split(", ")
list_two = input()

new_list = []
for i in list_one:
    if i in list_two:
        new_list.append(i)

# new_list = [i for i in list_one if i in list_two]
print(new_list)