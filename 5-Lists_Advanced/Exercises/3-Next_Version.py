current_version = input().split(".")
current_version = [int(n) for n in current_version]
current_version = int(''.join([str(elem) for elem in current_version]))

current_version += 1

print('.'.join(str(current_version)))


# Начин 2
# current_version = input().split(".")
# current_version = [int(n) for n in current_version]
#
# current_version[2] += 1
# if current_version[2] > 9:
#     current_version[2] = 0
#     current_version[1] += 1
#     if current_version[1] > 9:
#         current_version[1] = 0
#         current_version[0] += 1
# print('.'.join([str(elem) for elem in current_version]))

