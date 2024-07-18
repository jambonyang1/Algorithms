N = int(input())
array = list(map(int, input().split()))

dp = [1001] * N
dp[0] = 0

for i in range(0, N-1):
    for j in range(i+1, min(i + 1 + array[i], N)):
        dp[j] = min(dp[j], dp[i]+1)

print(dp[N-1] if dp[N-1] != 1001 else -1)