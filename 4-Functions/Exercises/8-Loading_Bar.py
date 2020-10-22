number = int(input())
new_number = number // 10


def loading_bar(number):
    dots = (10 - new_number) * "."
    percents = (10 - (10 - new_number)) * "%"
    if len(percents) < 10:
        return f"{number}% [{percents}{dots}]\nStill loading..."
    else:
        return f"100% Complete!\n[{percents}]"
print(loading_bar(number))