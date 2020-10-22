# Вариант в while цикъл започвайки търсенето на числото с обратна стъпка(отзад-напред) но с по-малко код/променливи:
divisor = int(input())
bound = int(input())

n = bound

while True:
    if n % divisor == 0:
        print(n)
        break
    else:
        n -= 1



# Вариант в while цикъл започвайки търсенето на числото с обратна стъпка(отзад-напред):
# divisor = int(input())
# bound = int(input())
#
# max_num = 0
# n = bound
#
# while True:
#     if n % divisor == 0:
#         max_num = n
#         break
#     n -= 1
# print(max_num)


# Вариант, в който започва търсенето на числото от последното т.е. с обратна стъпка(тоест, фор цикъла е с обратно броене):
# divisor = int(input())
# bound = int(input())
#
# max_num = 0
# n = 1
# for i in range(bound, 0, -1):
#     if n % divisor == 0:
#         max_num = n
#     n += 1
# print(max_num)

# Вариант, в който започва търсенето на числото от последното т.е. с обратна стъпка(тоест, фор цикъла е с обратно броене) но с по-малко код:
# divisor = int(input())
# bound = int(input())
#
# for i in range(bound, 0, -1):
#     if i % divisor == 0:
#         print(i)
#         break




# Вариант, в който започва търсенето на числото от първото такова:
# divisor = int(input())
# bound = int(input())
#
# max_num = 0
# n = 1
# for i in range(1, bound+1):
#     if n % divisor == 0:
#         max_num = n
#     n += 1
# print(max_num)