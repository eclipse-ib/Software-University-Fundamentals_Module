list_integers = input().split()
n = int(input())
list_integers = [int(i) for i in list_integers]

for i in range(n):
    list_integers.remove(min(list_integers))
print(list_integers)


