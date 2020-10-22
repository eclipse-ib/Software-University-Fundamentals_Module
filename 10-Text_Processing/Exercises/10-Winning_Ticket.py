def jackpot():
    if 10*"@" in first_half and 10*"@" in second_half:
        return ["True", "@", 10]
    elif 10*"#" in first_half and 10*"#" in second_half:
        return ["True", "#", 10]
    elif 10*"$" in first_half and 10*"$" in second_half:
        return ["True", "$", 10]
    elif 10*"^" in first_half and 10*"^" in second_half:
        return ["True", "^", 10]
    else:
        return ["False"]


def winning_symbols():
    if 9*"@" in first_half and 9*"@" in second_half:
        return ["@", 9]
    elif 8*"@" in first_half and 8*"@" in second_half:
        return ["@", 8]
    elif 7*"@" in first_half and 7*"@" in second_half:
        return ["@", 7]
    elif 6*"@" in first_half and 6*"@" in second_half:
        return ["@", 6]

    elif 9*"#" in first_half and 9*"#" in second_half:
        return ["#", 9]
    elif 8*"#" in first_half and 8*"#" in second_half:
        return ["#", 8]
    elif 7*"#" in first_half and 7*"#" in second_half:
        return ["#", 7]
    elif 6*"#" in first_half and 6*"#" in second_half:
        return ["#", 6]

    elif 9*"$" in first_half and 9*"$" in second_half:
        return ["$", 9]
    elif 8*"$" in first_half and 8*"$" in second_half:
        return ["$", 8]
    elif 7*"$" in first_half and 7*"$" in second_half:
        return ["$", 7]
    elif 6*"$" in first_half and 6*"$" in second_half:
        return ["$", 6]

    elif 9*"^" in first_half and 9*"^" in second_half:
        return ["^", 9]
    elif 8*"^" in first_half and 8*"^" in second_half:
        return ["^", 8]
    elif 7*"^" in first_half and 7*"^" in second_half:
        return ["^", 7]
    elif 6*"^" in first_half and 6*"^" in second_half:
        return ["^", 6]
    else:
        return "False"


tickets = [i.strip() for i in input().split(", ")]


for ticket in tickets:

    first_half = ticket[:((len(ticket))//2)]
    second_half = ticket[((len(ticket))//2):]

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    list_jackpot = jackpot()
    if list_jackpot[0] == 'True':
        print(f'ticket "{ticket}" - {list_jackpot[2]}{list_jackpot[1]} Jackpot!')
        continue

    if winning_symbols() == "False":
        print(f'ticket "{ticket}" - no match')
        continue

    if winning_symbols != "None":
        list_ws = winning_symbols()
        print(f'ticket "{ticket}" - {list_ws[1]}{list_ws[0]}')