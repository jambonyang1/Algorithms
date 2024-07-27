A = int(input())
li = list(map(int, input().split()))

dp = [li[0]]
for i in range(1, A):
    tmp = [li[i]]
    for j in range(i):
        if li[j] < li[i]:
            tmp.append(dp[j] + li[i])
    dp.append(max(tmp))

print(max(dp))
