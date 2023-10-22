N = int(input())
dp = [[0,0], [1,1], [1,1], [2, 2], [2,2], [3,3]]

for i in range(6, N+1):
    m = N
    M = 0
    for j in range(2, 6):
        m = min(m, dp[i-j][0] + dp[j][0])
        M = max(M, dp[i-j][1] + dp[j][1])
    dp.append([m, M])

print(dp[N][0], dp[N][1])