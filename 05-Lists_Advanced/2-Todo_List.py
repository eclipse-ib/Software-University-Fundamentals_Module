to_do_list = ["0"] * 10

while True:
    command = input().split("-", maxsplit=1)
    if "End" in command:
        break
    to_do_list.insert(int(command[0]), command[1])
while "0" in to_do_list:
    to_do_list.remove("0")
print(to_do_list)