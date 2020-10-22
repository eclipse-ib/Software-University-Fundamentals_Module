n = int(input())

res = [int(x) for x in str(n)]
res_reverse = sorted(res, reverse=True)
max_num = "".join(map(str, res_reverse))
print(max_num)