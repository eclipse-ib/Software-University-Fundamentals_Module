str_of_numbers = input()
number_of_beggars = int(input())
list_of_numbers = str_of_numbers.split(", ")
list_of_beggars = [0] * number_of_beggars

index_beg = 0
index_num = 0

for i in list_of_numbers:
    if index_beg > number_of_beggars-1:
        index_beg = 0
    list_of_beggars[index_beg] += int(i)
    index_beg += 1
    index_num += 1
print(f"{list_of_beggars}")