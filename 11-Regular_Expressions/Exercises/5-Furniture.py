import re

total_money_spend = 0
regex = r">>(?P<name>\w+)<<(?P<price>\d+((\.\d+)*))!(?P<count>\d+)\b"
print(f"Bought furniture:")
while True:
    command = input()
    if command == "Purchase":
        break
    matches = re.finditer(regex, command)
    for match in matches:
        if match:
            print(f'{match.group("name")}')
            if "." in match.group("price"):
                price = float(match.group("price"))
            else:
                price = int(match.group("price"))
            count = int(match.group("count"))
            total_money_spend += (price * count)
print(f"Total money spend: {total_money_spend:.2f}")