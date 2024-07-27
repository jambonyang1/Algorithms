N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = []

for i in range(N + 1):
    tmp = [0]
    for j in range(i):
        tj, pj = li[j]
        if j + tj <= i:
            tmp.append(dp[j] + pj)
        else:
            tmp.append(dp[j])
    dp.append(max(tmp))

print(max(dp))
