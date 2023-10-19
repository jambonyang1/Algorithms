n, m = map(int, input().split())

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(m):
        ii = i - 1
        jj = j - 1
        if ii >= 0:
            dp[i][j] += dp[ii][j]
        if jj >= 0:
            dp[i][j] += dp[i][jj]
        if ii >= 0 and jj >= 0:
            dp[i][j] += dp[ii][jj]

print((dp[n-1][m-1])%(10 ** 9 + 7))