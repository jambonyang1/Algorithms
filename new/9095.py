T = int(input())
ns = [int(input()) for _ in range(T)]

dp = [0, 1, 2, 4]
for i in range(4, max(ns) + 1):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

for n in ns:
    print(dp[n])
