resources = {}

while True:
    key = input()
    if key == "stop":
        break
    value = int(input())
    if key not in resources:
        resources[key] = 0
    resources[key] += value
for k, v in resources.items():
    print(f"{k} -> {v}")