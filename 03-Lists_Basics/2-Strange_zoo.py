## Решение по условие, в което е показано как се сменят отделните елементи в даден лист:
tail = input()
body = input()
head = input()

meerkat = [tail, body, head]
#№ meerkat[0], meerkat[-1] = meerkat[-1], meerkat[0]
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)


## Много опростен вариант:

tail = input()
body = input()
head = input()

meerkat = [head, body, tail]

print(meerkat)