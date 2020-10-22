n = int(input())

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            print(chr(96+a)+chr(96+b)+chr(96+c))