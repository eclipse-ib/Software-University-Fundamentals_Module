people = int(input())
lift = [int(i) for i in input().split()]

available_space = 0
for index,cabin in enumerate(lift):
    available_space = 4 - int(cabin)

    if people < 4:
        lift[index] += people
        people -= available_space
        break

    lift[index] += available_space
    people -= available_space


if people <= 0 and sum(lift) % 4 != 0:
    lift = [str(i) for i in lift]
    print(f"The lift has empty spots!")
    print(' '.join(lift))
elif sum(lift) % 4 == 0 and people > 0:
    lift = [str(i) for i in lift]
    print(f"There isn't enough space! {people} people in a queue!")
    print(' '.join(lift))
elif people <= 0 and sum(lift) == 0:
    lift = [str(i) for i in lift]
    print(f"The lift has empty spots!")
    print(' '.join(lift))
elif sum(lift) % 4 == 0 and people <= 0:
    lift = [str(i) for i in lift]
    print(' '.join(lift))
