n = int(input())
array = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i+1, n):
        if array[j] > array[i]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))