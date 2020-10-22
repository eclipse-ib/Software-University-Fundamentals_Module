followers = {}

while True:
    command = input().split(": ")
    if command[0] == "Log out":
        break

    username = command[1]

    if command[0] == "New follower":
        if username not in followers:
            followers[username] = (0, 0)

    elif command[0] == "Like":
        count = int(command[2])
        if username not in followers:
            followers[username] = (count, 0)
        else:
            followers[username] = ((followers[username])[0] + count, (followers[username])[1])

    elif command[0] == "Comment":
        if username not in followers:
            followers[username] = (0, 1)
        else:
            followers[username] = ((followers[username])[0], (followers[username])[1] + 1)

    elif command[0] == "Blocked":
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]

print(f"{len(followers)} followers")


for k, v in sorted(followers.items(), key=lambda item: item[1][0], reverse=True):
    print(f"{k}: {v[0] + v[1]}")