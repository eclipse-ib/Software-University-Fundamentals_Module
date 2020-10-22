#PB method with for loop:
# int_1 = int(input())
# int_2 = int(input())
# int_3 = int(input())
# int_4 = int(input())
#
# sum_2 = 0
#
# for i in range(1,4+1):
#     if i == 1 :
#         sum_2 += int_1
#     elif i == 2:
#         sum_2 += int_2
#     elif i == 3:
#         sum_2 = sum_2 // int_3
#     else:
#         sum_2 = sum_2 * int_4
# print(f"{sum_2}")


#Smarter method wioth no loops:
int_1 = int(input())
int_2 = int(input())
int_3 = int(input())
int_4 = int(input())

final_sum = ((int_1 + int_2) // int_3) * int_4
print(final_sum)
