number_of_trains = int(input())
number_trains_list = [0] * number_of_trains

command = input()
while command != "End":
    list_command = command.split()
    if list_command[0] == "add":
        number_trains_list[-1] += int(list_command[1])
    elif list_command[0] == "insert":
        number_trains_list[int(list_command[1])] += int(list_command[2])
    elif list_command[0] == "leave":
        number_trains_list[int(list_command[1])] -= int(list_command[2])
    command = input()
print(number_trains_list)