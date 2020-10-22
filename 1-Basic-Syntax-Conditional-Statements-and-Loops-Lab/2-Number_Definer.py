number = float(input())

##PB method:
# if number == 0:
#     print(f"zero")
# elif number > 0:
#     if number > 0 and number < 1:
#         print(f"small positive")
#     elif number > 1000000:
#         print(f"large positive")
#     else:
#         print(f"positive")
# else:
#     if number < 0 and number > -1:
#         print(f"small negative")
#     elif number < -1000000:
#         print(f"large negative")
#     else:
#         print(f"negative")

# New optimazed method:
# if number == 0:
#     print(f"zero")
# else:
#     if number > 0:
#         if number > 0 and number < 1:
#             print(f"small", end=" ")
#         elif number > 1_000_000:
#             print(f"large", end=" ")
#         print(f"positive")
#     else:
#         if number < 0 and number > -1:
#             print(f"small", end=" ")
#         elif number < -1000000:
#             print(f"large", end=" ")
#         print(f"negative")

# Super optimazed method:
if number == 0:
    print(f"zero")
else:
    if abs(number) < 1:
        print(f"small", end=" ")
    elif abs(number) > 1_000_000:
        print(f"large", end=" ")
    if number < 0:
        print(f"negative")
    elif number > 0:
        print(f"positive")
