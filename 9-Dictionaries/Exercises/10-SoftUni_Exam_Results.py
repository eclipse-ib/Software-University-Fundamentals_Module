submissions = {}
students_results = {}

while True:
    command = input().split("-")

    if command[0] == "exam finished":
        break

    student = command[0]
    if command[1] == "banned":
        del students_results[student]
        continue

    language = command[1]

    if language not in submissions:
        submissions[language] = 1
    else:
        submissions[language] += 1

    points = int(command[2])

    if student not in students_results:
        students_results[student] = {language: points}

    elif student in students_results:
        if language in students_results[student].keys():
            if points > (students_results[student])[language]:
                (students_results[student])[language] = points
        else:
            students_results[student].update({language: points})

print(f"Results:")

max_students_results = {}
for user, result in students_results.items():
    max_result = 0

    for key, value in result.items():
        if value >= max_result:
            max_result = value
        max_students_results[user] = int(max_result)
        break

for name, max_result in sorted(max_students_results.items(), key=lambda item: (-item[1], item[0])):
    print(f"{name} | {max_result}")

print(f"Submissions:")
for language, submissions_count in sorted(submissions.items(),
                                          key=lambda item: (-item[1], item[0])):
    print(f"{language} - {submissions_count}")