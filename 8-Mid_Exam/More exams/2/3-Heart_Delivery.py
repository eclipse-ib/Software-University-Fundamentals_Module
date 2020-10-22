neighborhood = [int(i) for i in input().split("@")]

cupid_start_position = 0
cupid_last_position = 0

while True:
    command_no_splt = input()
    if command_no_splt == "Love!":
        break
    command = command_no_splt.split()

    index = cupid_start_position + int(command[1])
    cupid_start_position = int(command[1])
    cupid_last_position = index

    if index <= (len(neighborhood)-1):
        if neighborhood[index] == 0:
            print(f"Place {index} already had Valentine's day.")
        else:
            neighborhood[index] -= 2
            if neighborhood[index] == 0:
                print(f"Place {index} has Valentine's day.")

    elif index > (len(neighborhood)-1):
        cupid_start_position = 0
        cupid_last_position = 0
        if neighborhood[cupid_start_position] == 0:
            print(f"Place {cupid_start_position} already had Valentine's day.")
        else:
            neighborhood[cupid_start_position] -= 2

            if neighborhood[cupid_start_position] == 0:
                print(f"Place {cupid_start_position} has Valentine's day.")

print(f"Cupid's last position was {cupid_last_position}.")

vdays = 0
for v_day in neighborhood:
    if v_day <= 0:
        vdays += 1
if vdays == len(neighborhood):
    print(f"Mission was successful.")
else:
    count_no_vdays_houses = len(neighborhood) - vdays
    print(f"Cupid has failed {count_no_vdays_houses} places.")
