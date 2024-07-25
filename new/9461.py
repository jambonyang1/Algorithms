T = int(input())
ns = []
for _ in range(T):
    ns.append(int(input()))
dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, max(ns) + 1):
    dp.append(dp[i - 1] + dp[i - 5])

for n in ns:
    print(dp[n])
