rooms = int(input())

free_chairs = 0
for room in range(1, rooms+1):
    chairs = input().split()
    needed_chairs = 0
    if len(chairs[0]) > int(chairs[1]):
        free_chairs += (len(chairs[0]) - int(chairs[1]))
    elif len(chairs[0]) < int(chairs[1]):
        needed_chairs += (int(chairs[1]) - len(chairs[0]))
        free_chairs -= needed_chairs
        print(f"{needed_chairs} more chairs needed in room {room}")
if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
