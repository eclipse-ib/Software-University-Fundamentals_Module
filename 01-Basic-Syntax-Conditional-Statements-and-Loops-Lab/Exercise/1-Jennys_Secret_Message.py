#PB method:
name = input().lower()
if name == "johnny":
    print(f"Hello, my love!")
else:
    print(f"Hello, {name.capitalize()}!")

# PB method with just one print():
name = input()
if name == "Johnny":
    name = "my love"
print(f"Hello, {name}!")