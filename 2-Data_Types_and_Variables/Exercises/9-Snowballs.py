n = int(input())

first = 0
second = 0
third = 0
snowball_value = 0
for i in range(1, n+1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_snowball_value = (snowball_snow // snowball_time) ** snowball_quality
    if current_snowball_value > snowball_value:
        first = snowball_snow
        second = snowball_time
        third = snowball_quality
        snowball_value = current_snowball_value
print(f"{first} : {second} = {snowball_value} ({third})")
