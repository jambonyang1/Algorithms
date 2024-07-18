N, M = map(int, input().split())

dp = [1, 0, 1]

for i in range(3, max(N,M)+1):
    ans = 0
    for j in range(1, i // 2 + 1):
        if not dp[j] and not dp[i-j]:
            ans = 1
            break
    dp.append(ans)


print("A" if dp[N] or dp[M] else "B")