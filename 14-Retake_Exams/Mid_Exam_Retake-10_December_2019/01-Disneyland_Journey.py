journey_cost = float(input())
months = int(input())

saved_money = 0

for i in range(1, months+1):

    if i % 2 != 0 and i != 1:
        saved_money = saved_money * 0.84

    if i % 4 == 0:
        saved_money = saved_money * 1.25

    saved_money += journey_cost / 4

diff = abs(journey_cost - saved_money)
if saved_money >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {diff:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {diff:.2f}lv. more.")