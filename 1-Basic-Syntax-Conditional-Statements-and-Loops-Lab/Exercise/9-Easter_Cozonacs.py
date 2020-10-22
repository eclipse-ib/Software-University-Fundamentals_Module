budget = float(input())
one_kg_flour = float(input())

one_egg_pack = one_kg_flour * 0.75
one_liter_milk = one_kg_flour * 1.25
one_cozonac_recipe = one_kg_flour + one_egg_pack + (one_liter_milk / 4)

made_cozunacs = 0
colored_eggs = 0

while budget > one_cozonac_recipe:
    budget -= one_cozonac_recipe
    made_cozunacs += 1
    colored_eggs += 3
    if made_cozunacs % 3 == 0:
        colored_eggs = colored_eggs - (made_cozunacs-2)

print(f"You made {made_cozunacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")