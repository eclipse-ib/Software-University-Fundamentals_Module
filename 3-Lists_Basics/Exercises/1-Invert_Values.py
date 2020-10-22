s = input()
separated_s = s.split(" ")
new_list = []

for l in separated_s:
    number = -int(l)
    new_list.append(number)
print(new_list)


## Моето решение на задачата:
# s = input()
# separated_s = s.split(" ")
# new_list = []
#
# for l in separated_s:
#     if int(l) < 0:
#         new_list.append(abs(int(l)))
#     elif int(l) >= 0:
#         new_list.append(int("-"+l))
#
# print(new_list)



## PB опит, неуспешен - 60/100 в judge:
# s = input()
# new_s = []
# count = 0
#
# for l in s:
#     if count == 1:
#         new_s.append(int(l))
#         count = 0
#         continue
#     if l == " ":
#         continue
#     elif l == "-":
#         count +=1
#         continue
#     elif int(l) < 0:
#         new_s.append(int(l))
#     elif int(l) >= 0:
#         new_s.append(int("-"+l))
#
# print(new_s)