N = int(input())
array = list(map(int, input().split()))

dp = [1] * N

for i in range(N-1):
    for j in range(i+1, N):
        if array[i] < array[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))