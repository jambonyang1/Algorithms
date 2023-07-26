N, M = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

D = [10001] * (M+1)

D[0] = 0
for i in range(1, M+1):
    tmp = [D[i]]
    for coin in coins:
        if i - coin >= 0:
            tmp.append(D[i-coin] + 1)
    D[i] = min(tmp)

if D[M] == 10001:
    print(-1)
else:
    print(D[M])