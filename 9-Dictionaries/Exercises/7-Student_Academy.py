rows = int(input())

students = {}

for row in range(0, (2 * rows), 2):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

students_with_high_grades = {}
for key, value in students.items():
    if (sum(value) / len(value)) >= 4.50:
        students_with_high_grades[key] = sum(value) / len(value)
for name, grade in sorted(students_with_high_grades.items(), key=lambda item: -item[1]):
    print(f"{name} -> {grade:.2f}")