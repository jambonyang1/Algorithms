N = int(input())

dp = [0, 1]

for i in range(2, N+1):
    if int(i ** (1/2)) ** 2 == i:
        dp.append(1)
        continue

    tmp = i
    for j in range(int(i ** (1/2)), 0, -1):
        tmp = min(tmp, dp[i - j**2]+1)
    dp.append(tmp)

print(dp[N])