N = int(input())
array = list(map(int, input().split()))

dp = [1] * N
for i in range(N-1):
    now = array[i]
    for j in range(i+1, N):
        if array[j] > now:
            dp[j] = max(dp[i]+1, dp[j])

print(max(dp))