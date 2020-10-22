elements = input().split()
moves = 0

while True:
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
    command_no_splt = input()
    if len(elements) != 0 and command_no_splt == "end":
        print(f"Sorry you lose :(\n{' '.join(elements)}")
        break
    if command_no_splt == "end":
        break

    command = command_no_splt.split()
    index_one = command[0]
    index_two = command[1]

    # cheat detect start
    if (
        index_one == index_two or
        int(index_one) > len(elements) or
        int(index_one) < 0 or
        int(index_two) > len(elements) or
        int(index_two) < 0
    ):
        moves += 1
        elements.insert(len(elements)//2, f"-{moves}a")
        elements.insert(len(elements) // 2, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue
    # cheat detect end

    if elements[int(index_one)] == elements[int(index_two)]:
        print(f"Congrats! You have found matching elements - {elements[int(index_one)]}!")
        elements = [e for e in elements if e not in (elements[int(index_one)], [int(index_two)])]
        moves += 1
    elif elements[int(index_one)] != elements[int(index_two)]:
        print("Try again!")