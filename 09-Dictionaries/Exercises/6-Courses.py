courses = {}

while True:
    command = input().split(" : ", maxsplit=2)
    if command[0] == "end":
        break
    course_name = command[0]
    student_name = command[1]
    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)


# for key, value in sorted(courses.items(), key=lambda item: len(item[1]), reverse=True):
#     print(f"{key}: {len(value)}")
#     for names in sorted(value):
#         print(f"-- {names}")
for course in sorted(courses.items(), key=lambda item: len(item[1]), reverse=True):
    students_in_course = len(course[1])
    print(f"{course[0]}: {students_in_course}")
    for v in sorted(course[1]):
        print(f"-- {v}")