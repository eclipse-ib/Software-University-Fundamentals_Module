n = int(input())

heroes = {}

for _ in range(n):
    hero_info = input().split()
    hero_name = hero_info[0]
    hit_points = int(hero_info[1])
    mana_points = int(hero_info[2])

    heroes[hero_name] = {}
    heroes[hero_name]["HP"] = hit_points
    heroes[hero_name]["MP"] = mana_points

while True:
    commands = input().split(' - ')
    command = commands[0]

    if command == "End":
        break

    name = commands[1]

    if command == "CastSpell":
        MP_needed = int(commands[2])
        spell_name = commands[3]

        if heroes[name]["MP"] >= MP_needed:
            heroes[name]["MP"] -= MP_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['MP']} MP!")

        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(commands[2])
        attacker = commands[3]
        heroes[name]["HP"] -= damage
        if heroes[name]["HP"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]

    elif command == "Recharge":
        amount = int(commands[2])
        if heroes[name]['MP'] + amount <= 200:
            print(f"{name} recharged for {amount} MP!")
            heroes[name]['MP'] += amount
        else:
            recovery_amount = amount - ((heroes[name]['MP'] + amount) - 200)
            print(f"{name} recharged for {recovery_amount} MP!")
            heroes[name]['MP'] = 200

    elif command == "Heal":
        heal_amount = int(commands[2])
        if heroes[name]['HP'] + heal_amount <= 100:
            print(f"{name} healed for {heal_amount} HP!")
            heroes[name]['HP'] += heal_amount
        else:
            h_amount = heal_amount - ((heroes[name]['HP'] + heal_amount) - 100)
            print(f"{name} healed for {h_amount} HP!")
            heroes[name]['HP'] = 100

sorted_heroes = sorted(heroes.keys(), key=lambda h: (-heroes[h]['HP'], h))

for key in sorted_heroes:
    print(f"{key}\n  HP: {heroes[key]['HP']}\n  MP: {heroes[key]['MP']}")
