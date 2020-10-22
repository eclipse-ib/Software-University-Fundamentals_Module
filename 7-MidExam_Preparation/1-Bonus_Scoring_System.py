import math
students = int(input())
lectures = int(input())
additional_bonus = int(input())

total_max_bonus = 0
max_student_attendances = 0

for i in range(students):
    student_attendances = int(input())
    total_bonus = (student_attendances / lectures) * (5 + additional_bonus)
    if total_bonus > total_max_bonus:
        total_max_bonus = total_bonus
        max_student_attendances = student_attendances

print(f"Max Bonus: {math.ceil(total_max_bonus)}.\n"
f"The student has attended {max_student_attendances} lectures."
)