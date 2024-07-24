import sys

input = sys.stdin.readline

T = int(input())
cases = []
M = 0
m = 0
for _ in range(T):
    a, b = map(int, input().split())
    M = max(M, b)
    m = max(m, a)
    cases.append([a, b])

dp = [[0 for _ in range(M + 1)] for _ in range(M + 1)]
for i in range(1, M + 1):
    dp[i][i] = 1
    dp[1][i] = i

for i in range(2, m + 1):
    for j in range(i + 1, M + 1):
        now = 0
        for k in range(j - i + 1):
            now += dp[i - 1][j - k - 1]
        dp[i][j] = now

for a, b in cases:
    print(dp[a][b])
