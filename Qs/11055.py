N = int(input())
array = list(map(int, input().split()))

dp = []
for i in array:
    dp.append(i)

for i in range(0, N-1):
    for j in range(i+1, N):
        if array[j] > array[i]:
            dp[j] = max(dp[j], dp[i] + array[j])

print(max(dp))