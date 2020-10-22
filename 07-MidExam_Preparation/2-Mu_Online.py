dungeons_rooms = input().split("|")

health = 100
bitcoins = 0
rooms_count = 0

for i in dungeons_rooms:
    room = i.split(" ")

    if room[0] == "potion":
        amount = int(room[1])
        exceed_health = health + amount
        if exceed_health > 100:
            amount = amount-(exceed_health-100)
        health += int(room[1])
        if health > 100:
            health = 100
        rooms_count += 1
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif room[0] == "chest":
        bitcoins += int(room[1])
        rooms_count += 1
        print(f"You found {room[1]} bitcoins.")

    else:
        health -= int(room[1])
        rooms_count += 1
        if health > 0:
            print(f"You slayed {room[0]}.")
        else:
            print(f"You died! Killed by {room[0]}.")
            print(f"Best room: {rooms_count}")
            exit()

print(
    f"You've made it!\n"
    f"Bitcoins: {bitcoins}\n"
    f"Health: {health}"
)