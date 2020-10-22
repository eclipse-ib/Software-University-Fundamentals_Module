party_size = int(input())
days = int(input())

earning = 0

for i in range(1, days+1):
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5
        earning -= party_size * 2
    earning += 50 - (party_size*2)
    if i % 3 == 0:
        earning -= party_size*3
    if i % 5 == 0:
        earning += party_size*20

coins_each = earning // party_size
print(f"{party_size} companions received {coins_each} coins each.")