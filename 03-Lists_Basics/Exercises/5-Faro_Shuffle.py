cards = input().split()
number_of_decks = int(input())
middle_lenght = len(cards) // 2

for i in range(number_of_decks):
    res = []

    for index in range(middle_lenght):
        first_card = cards[index]

        current_index_second_deck = index + middle_lenght
        second_card = cards[current_index_second_deck]

        res.append(first_card)
        res.append(second_card)
    cards = res
print(cards)




# index_one = 0
# index_two = len(string_list) // 2
#
#
# for deck in range(0,number_of_decks):
#     for half_one in range(0, (len(string_list) // 2)):
#         for half_two in range((len(string_list) // 2), len(string_list)+1):
#             print(string_list[half_one], string_list[half_two], end="")
#             index_one += 1
