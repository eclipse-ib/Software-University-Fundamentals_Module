str_one = input()
str_two = input()

for i in range(len(str_one)):
    if str_one[i] != str_two[i]:
        for str_two_index in range(0, i+1):
            print(str_two[str_two_index], end="")
        for str_one_index in range(i+1, len(str_one)):
            print(str_one[str_one_index], end="")
        print()
#PB method with 3 loops

# #PB metho with one FOR loop:
# string_one = input()
# string_two = input()
#
# c_i = 0
# same_str = 1
# str_ind = 1
#
# for i in string_one:
#     if string_one[c_i] != string_two[c_i]:
#         if c_i == 0:
#             print(string_two[c_i] + string_one[same_str:len(string_one)])
#             c_i += 1
#             same_str += 1
#             continue
#         elif str_ind == 0:
#             print(string_two[str_ind] + string_two[c_i] + string_one[same_str:len(string_one)])
#             str_ind += 1
#             c_i += 1
#             same_str += 1
#             continue
#         else:
#             print(string_two[0:c_i] + string_two[c_i] + string_one[same_str:len(string_one)])
#             str_ind += 1
#             c_i += 1
#             same_str += 1
#             continue
#     else:
#         c_i += 1
#         same_str += 1
#         str_ind += 1