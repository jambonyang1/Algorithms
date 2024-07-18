import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        a, b, c = 20, 20, 20
    
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                if i < j and j < k:
                    dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
    return dp[a][b][c]

dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')