# PB method:
# import math
# centuries = int(input())
#
# years = centuries * 100
# days = math.floor(years * 365.2422)
# hours = days * 24
# minutes = hours * 60
#
# print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")

# New method with constants:
# import math
#
# MINUTES_IN_ONE_HOUR = 60
# HOURS_IN_ONE_DAY = 24
# DAYS_IN_ONE_YEAR = 365.2422
# YEARS_IN_ONE_CENTURY = 100
#
# centuries = int(input())
#
# years = centuries * YEARS_IN_ONE_CENTURY
# days = math.floor(years * DAYS_IN_ONE_YEAR)
# hours = days * HOURS_IN_ONE_DAY
# minutes = hours * MINUTES_IN_ONE_HOUR
#
# print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")



# New and smarter method by casting the float number to integer( on line 40 ):
MINUTES_IN_ONE_HOUR = 60
HOURS_IN_ONE_DAY = 24
DAYS_IN_ONE_YEAR = 365.2422
YEARS_IN_ONE_CENTURY = 100

centuries = int(input())

years = centuries * YEARS_IN_ONE_CENTURY
days = int(years * DAYS_IN_ONE_YEAR)
hours = days * HOURS_IN_ONE_DAY
minutes = hours * MINUTES_IN_ONE_HOUR

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")