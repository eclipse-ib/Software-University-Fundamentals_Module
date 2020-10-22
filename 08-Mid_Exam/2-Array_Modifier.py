arrays = [i for i in input().split()]


def swap():
    arrays[int(command[1])], arrays[int(command[2])] \
        = arrays[int(command[2])], arrays[int(command[1])]


def multiply():
    arrays[int(command[1])] = str(int(arrays[int(command[1])]) * int(arrays[int(command[2])]))


def decrease():
    arrays[:] = [str(int(number)-1) for number in arrays]


while True:
    command_no_splt = input()
    if command_no_splt == "end":
        break
    command = command_no_splt.split()
    if command[0] == "swap":
        swap()
    elif command[0] == "multiply":
        multiply()
    elif command[0] == "decrease":
        decrease()

print(", ".join(arrays))