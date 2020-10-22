string = input()
new_string = ""
next_index = ""
momment_index = 0
for index, character in enumerate(string):
    if next_index:
        next_index = False
        continue
    if character.isdigit():
        multiply_number = int(character)
        if int(string[index]) != int(string[-1]):
            if string[index+1].isdigit():
                multiply_number = string[index] + string[index+1]
                new_string += string[momment_index:index].upper() * int(multiply_number)
                momment_index = index+1
                next_index = True
                continue
        new_string += string[momment_index:index].upper() * multiply_number
        momment_index = index
        next_index = False

final_string = ""
for i in new_string:
    if i.isdigit():
        continue
    final_string += i

unique_symbols = len(set(final_string))

print(f"Unique symbols used: {unique_symbols}")
print(final_string)