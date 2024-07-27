A = int(input())
li = list(map(int, input().split()))

dp = [1]
for i in range(1, A):
    tmp = [1]
    for j in range(i):
        if li[j] > li[i]:
            tmp.append(dp[j] + 1)
    dp.append(max(tmp))

print(max(dp))
