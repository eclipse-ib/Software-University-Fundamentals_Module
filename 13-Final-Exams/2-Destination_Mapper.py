import re

places = input()

regex = r"(=|\/)([A-Z][A-Za-z]{2,})\1"

# matches = re.findall(regex, places)
places = [match[1] for match in re.findall(regex, places)]

print(f"Destinations: {', '.join(places)}")
print(f"Travel Points: {len(''.join(places))}")