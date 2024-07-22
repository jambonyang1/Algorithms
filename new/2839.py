N = int(input())

dp = [0, -1, -1]
for i in range(3, N + 1):
    tmp = []
    if dp[i - 3] != -1:
        tmp.append(dp[i - 3] + 1)
    if i - 5 >= 0:
        if dp[i - 5] != -1:
            tmp.append(dp[i - 5] + 1)
    if len(tmp) == 0:
        dp.append(-1)
    else:
        dp.append(min(tmp))

print(dp[N])
