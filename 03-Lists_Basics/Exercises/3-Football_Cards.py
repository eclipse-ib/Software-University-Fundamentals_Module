cards = input().split()
team_a_players = list(range(1, 11+1))
team_b_players = list(range(1, 11+1))

for card in cards:
    tokens = card.split("-")
    team = tokens[0]
    number = int(tokens[1])
    if "A" in tokens:
        if number > 0 and number < 12 and number not in team_a_players:
            continue
        team_a_players.remove(number)
    else:
        if number > 0 and number < 12 and number not in team_b_players:
            continue
        team_b_players.remove(number)
if len(team_a_players) < 7 or len(team_b_players) < 7:
    print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")
    print(f"Game was terminated")
    exit()
print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")


## Мой опит за решение:
# cards = input().split()
# team_a_players = list(range(1, 11+1))
# team_b_players = list(range(1, 11+1))
#
# for i in cards:
#     str_current_card = "".join(i)
#     current_card = str_current_card.split()
#     if len(team_a_players) < 7 or len(team_b_players) < 7:
#         print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")
#         print(f"Game was terminated")
#         break
#     if "A" in i:
#         current_card.pop(0)
#         current_card.pop(1)
#         team_a_players.remove(str(current_card))
#     elif "A" in i:
#         current_card.pop(0)
#         current_card.pop(1)
#         team_b_players.remove(str(current_card))
#
#
# print(team_a_players, team_b_players)