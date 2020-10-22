## PB method :
# n = int(input())
#
# positive = []
# negative = []
# count_positives = 0
# negative_sum = 0
#
# for i in range(1, n+1):
#     number = int(input())
#     if number >= 0:
#         positive.append(number)
#         count_positives += 1
#     else:
#         negative.append(number)
#         negative_sum += number
# # print(positive)
# # print(negative)
# # print(f"Count of positives: {count_positives}. Sum of negatives: {negative_sum}")
# ## New print method by using \n :
# print(f"{positive}\n{negative}\nCount of positives: {count_positives}. Sum of negatives: {negative_sum}")


## Нов метод с изчисленията на последните две променливи използвайки len() и sum():

n = int(input())

positive = []
negative = []

for i in range(1, n+1):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
count_positives = len(positive)
negative_sum = sum(negative)
print(positive)
print(negative)
print(f"Count of positives: {count_positives}. Sum of negatives: {negative_sum}")
# print(f"{positive}\n{negative}\nCount of positives: {count_positives}. Sum of negatives: {negative_sum}")