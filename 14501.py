N = int(input())
table = []
for i in range(N):
    table.append(list(map(int, input().split())))

dp = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i+table[i][0], N+1):
        if dp[j] < dp[i] + table[i][1]:
            dp[j] = dp[i] + table[i][1]

print(dp[-1])