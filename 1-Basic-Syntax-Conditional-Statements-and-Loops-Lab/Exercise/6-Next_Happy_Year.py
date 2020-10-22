# New method by using an function set():
year = int(input())

year_nums = len(str(year))
next_year = year + 1

while True:
    s = set(str(next_year))  # Creates a set of Unique Un-Ordered Elements
    l = len(s)  # It returns the length of the above set.
    if year_nums == 4 and l == 4:
        print(str(next_year))
        break
    elif year_nums == 3 and l == 3:
        print(str(next_year))
        break
    next_year += 1

# PB method:
# year = int(input())
#
# next_year = year + 1
#
# if len(str(year)) == 4:
#     while True:
#         if str(next_year)[0] != str(next_year)[1] and str(next_year)[0] != str(next_year)[2]\
#                 and str(next_year)[0] != str(next_year)[3] and str(next_year)[1] != str(next_year)[2]\
#                 and str(next_year)[1] != str(next_year)[3] and str(next_year)[2] != str(next_year)[3]:
#             print(next_year)
#             break
#         next_year += 1
# elif len(str(year)) == 3:
#     while True:
#         if str(next_year)[0] != str(next_year)[1] and str(next_year)[0] != str(next_year)[2]\
#                 and str(next_year)[1] != str(next_year)[2]:
#             print(next_year)
#             break
#         next_year += 1
