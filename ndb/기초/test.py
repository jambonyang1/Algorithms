N, M = map(int, input().split())
d = [10001] * (M+1)
moneys = []
for _ in range(N):
    money = int(input())
    moneys.append(money)
    if money <= M:
        d[money] = 1

for i in range(min(moneys) + 1, M+1):
    tmp = [d[i]]
    for mon in moneys:
        if i - mon > 0:
            tmp.append(d[i-mon] + 1)
    d[i] = min(tmp)


print(d[M+1])
