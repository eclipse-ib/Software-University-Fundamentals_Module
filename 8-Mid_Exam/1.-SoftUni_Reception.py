import math

employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
students_count = int(input())


total_answers_per_hour = (
        employee_1 +
        employee_2 +
        employee_3
        )

hours = 0
needed_hours = 0
while True:
    if students_count <= 0:
        break
    hours += 1
    if hours % 4 == 0:
        needed_hours += 1
        continue
    students_count -= total_answers_per_hour
    needed_hours += 1

print(f"Time needed: {math.ceil(needed_hours)}h.")