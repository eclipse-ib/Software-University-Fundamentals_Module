companies = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break
    company = command[0]
    user = command[1]
    if company not in companies:
        companies[company] = [user]
    else:
        if user not in companies[company]:
            companies[company].append(user)

for key, value in sorted(companies.items(), key=lambda item: item[0]):
    print(f"{key}")
    for user in value:
        print(f"-- {user}")