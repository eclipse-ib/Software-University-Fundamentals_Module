collection = input().split()

while True:
    commands = input().split()

    command = commands[0]

    if command == "end":
        break

    if command == "reverse":
        reverse_from = int(commands[2])
        reverse_to = int(commands[4])
        # part_one = collection[:reverse_from]
        # part_two = collection[reverse_from:reverse_to+2]
        # part_two.reverse()
        # part_three = collection[reverse_to+2:]
        # collection = part_one + part_two + part_three
        collection = collection[:reverse_from] + collection[reverse_to+1:reverse_from-1:-1]\
                     + collection[reverse_to+2:]

    elif command == "sort":
        sort_from = int(commands[2])
        sort_to = int(commands[4])
        # part_one_s = collection[:sort_from]
        # part_two_s = collection[sort_from:sort_to + 2]
        # part_two_s.sort()
        # part_three_s = collection[sort_to + 2:]
        # collection = part_one_s + part_two_s + part_three_s
        collection = collection[:sort_from] + sorted(collection[sort_to+1:sort_from-1:-1]) \
                     + collection[sort_to + 2:]

    elif command == "remove":
        remove_count = int(commands[1])
        collection = collection[remove_count:]

print(', '.join(collection))