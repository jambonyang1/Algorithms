import sys
input = sys.stdin.readline

N = int(input())
table = list()
for _ in range(N):
    table.append(list(map(int, input().split())))

dp = [[0 for i in range(N)] for j in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] == 0 or table[i][j] == 0:
            continue
        value = dp[i][j]
        length =  table[i][j]
        if i + length< N:
            dp[i + length][j] += value
        if j + length < N:
            dp[i][j + length] += value

print(dp[-1][-1])