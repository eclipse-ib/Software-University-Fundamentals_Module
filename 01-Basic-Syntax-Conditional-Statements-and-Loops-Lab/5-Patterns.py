# PB method with 1 FOR loop: НАЙ-ДОБРИЯ измислен от мен.
n = int(input())

star_up = 1
star_down = n-1

for i in range(1, n*2):
    if i > n:
        print(star_down * "*")
        star_down -= 1
        continue
    print(star_up * "*")
    star_up += 1


# PB method with 2 FOR loops:
# n = int(input())
#
# star = 1
#
# for i in range(1, n+1):
#     print(star * "*")
#     star += 1
#
# star = n-1
#
# for j in range(n-1, 0, -1):
#     print(star * "*")
#     star -= 1


number = int(input())
for i in range(1, number, +1):
    for j in range(0, i):
        print('*', end='')
    print()
for i in range(number -1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()