line_one = input().split(" ")
line_two = input().split(" ")
line_three = input().split(" ")

player_1_won = (
    #horizontal
    (line_one[0] == "1" and line_one[1] == "1" and line_one[2] == "1" or
    line_two[0] == "1" and line_two[1] == "1" and line_two[2] == "1" or
    line_three[0] == "1" and line_three[1] == "1" and line_three[2] == "1") or
    #vertical
    (line_one[0] == "1" and line_two[0] == "1" and line_three[0] == "1" or
    line_one[1] == "1" and line_two[1] == "1" and line_three[1] == "1" or
    line_one[2] == "1" and line_two[2] == "1" and line_three[2] == "1") or
    #diagonal
    (line_one[0] == "1" and line_two[1] == "1" and line_three[2] == "1" or
    line_three[0] == "1" and line_two[1] == "1" and line_one[2] == "1")
)

player_2_won = (
    #horizontal
    (line_one[0] == "2" and line_one[1] == "2" and line_one[2] == "2" or
    line_two[0] == "2" and line_two[1] == "2" and line_two[2] == "2" or
    line_three[0] == "2" and line_three[1] == "2" and line_three[2] == "2") or
    #vertical
    (line_one[0] == "2" and line_two[0] == "2" and line_three[0] == "2" or
    line_one[1] == "2" and line_two[1] == "2" and line_three[1] == "2" or
    line_one[2] == "2" and line_two[2] == "2" and line_three[2] == "2") or
    #diagonal
    (line_one[0] == "2" and line_two[1] == "2" and line_three[2] == "2" or
    line_three[0] == "2" and line_two[1] == "2" and line_one[3] == "2")
)
if player_1_won:
    print(f"First player won")
elif player_2_won:
    print(f"Second player won")
else:
    print(f"Draw!")